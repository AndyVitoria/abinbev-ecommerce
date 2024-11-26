from typing import Union
from datetime import timedelta

from src.repositories.models import UserModel
from src.repositories.interface import SQLLiteInterface
from src.entities import User, Token
from src.utils import CryptUtils, FakerVault


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
        self.__user_model = self.__get_user_model()
        if isinstance(self.__user_model, UserModel) and self.__verify_password():
            access_token = self.__crypt_utils.create_access_token(
                data={"sub": self.__user.username},
            )
            return Token(access_token=access_token, token_type="bearer")
        else:
            raise ValueError("Invalid username or password")

    def __verify_password(self):
        return self.__crypt_utils.verify_password(
            plain_password=self.__user.password.get_secret_value(),
            hashed_password=self.__user_model.password,
        )

    def __get_user_model(self):
        query_result = self.__database_interface.where(
            model_class=UserModel,
            condition=(
                (UserModel.username == self.__user.username)
                & (UserModel.is_active == True)
            ),
        ) + [None]

        return query_result.pop(0)
