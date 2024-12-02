from typing import Union
from datetime import timedelta

from src.repositories.models import UserModel
from src.repositories.interface import SQLLiteInterface
from src.entities import User, Token
from src.utils import CryptUtils, FakerVault
from src.exceptions import AuthenticationError, NotFoundError


class LoginUseCase:
    def __init__(self, user: User):
        self.__user = user
        self.__database_interface = SQLLiteInterface()
        self.__user_model: Union[UserModel, None] = None
        vault = FakerVault()
        self.__crypt_utils = CryptUtils(
            vault.get_secret("SECRET_KEY"),
            vault.get_secret("ALGORITHM"),
            vault.get_secret("ACCESS_TOKEN_EXPIRE_MINUTES"),
        )

    def generate_token(self):
        self.__user_model = self.__get_user_model(
            username=self.__user.username, database_interface=self.__database_interface
        )
        if isinstance(self.__user_model, UserModel) and self.__verify_password():
            access_token = self.__crypt_utils.create_access_token(
                data={
                    "username": self.__user.username,
                    "id": self.__user_model.id,
                },
            )
            return Token(access_token=access_token, token_type="bearer")
        else:
            raise AuthenticationError("Invalid credentials")

    def __verify_password(self):
        return self.__crypt_utils.verify_password(
            plain_password=self.__user.password.get_secret_value(),
            hashed_password=self.__user_model.password,
        )

    # TODO: Move to a appropriate class
    @staticmethod
    def __get_user_model(username, database_interface):
        query_result = database_interface.where(
            model_class=UserModel,
            condition=(
                (UserModel.username == username) & (UserModel.is_active == True)
            ),
        ) + [None]

        return query_result.pop(0)

    # TODO: Move to a appropriate class
    @classmethod
    def decode_token_to_user(cls, token: str) -> User:
        vault = FakerVault()
        crypt_utils = CryptUtils(
            vault.get_secret("SECRET_KEY"),
            vault.get_secret("ALGORITHM"),
            vault.get_secret("ACCESS_TOKEN_EXPIRE_MINUTES"),
        )
        if crypt_utils.is_token_expired(token):
            raise AuthenticationError("Token expired")
        data = crypt_utils.decode_access_token(token)
        database_interface = SQLLiteInterface()
        user_model = cls.__get_user_model(data.get("username"), database_interface)

        if user_model is not None:
            return User(
                id=user_model.id,
                username=user_model.username,
                email=user_model.email,
                password=user_model.password,
                is_superuser=user_model.is_superuser,
            )
        else:
            raise NotFoundError("User")
