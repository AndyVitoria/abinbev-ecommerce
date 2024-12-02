from sqlmodel import SQLModel, Field
from hashlib import sha256

from src.entities.users import User
from src.utils import FakerVault, CryptUtils


class UserModel(SQLModel, table=True):
    """UserModel is a SQLModel representation of the User entity"""

    id: int = Field(primary_key=True)
    username: str
    email: str
    password: str
    is_active: bool = True
    is_superuser: bool = False

    @classmethod
    def from_entity(cls, entity: User):
        """Creates an instance of UserModel based on the User entity provided

        Parameters
        ----------
        entity: User
            The user entity to be converted to a UserModel

        Returns
        -------
        UserModel
            The UserModel created based on the User entity provided
        """
        vault = FakerVault()
        crypt_utils = CryptUtils(
            vault.get_secret("SECRET_KEY"),
            vault.get_secret("ALGORITHM"),
            vault.get_secret("ACCESS_TOKEN_EXPIRE_MINUTES"),
        )
        return cls(
            id=entity.id,
            username=entity.username,
            email=entity.email,
            password=crypt_utils.hash_password(entity.password.get_secret_value()),
            is_superuser=entity.is_superuser,
        )

    def to_entity(self):
        """Creates an instance of User based on the UserModel provided

        Returns
        -------
        User
            The User created based on the UserModel provided
        """
        return User(
            id=self.id,
            username=self.username,
            email=self.email,
            password=self.password,
            is_active=self.is_active,
            is_superuser=self.is_superuser,
        )
