from sqlmodel import SQLModel, Field
from hashlib import sha256

from src.entities.users import User


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
        return cls(
            username=entity.username,
            email=entity.email,
            password=sha256(entity.password.get_secret_value().encode()).hexdigest(),
            is_superuser=entity.is_superuser,
        )
