from src.entities import User
from src.repositories.models import UserModel
from src.repositories.interface import SQLLiteInterface
from src.repositories.database import SQLLiteDatabaseMonostate
from .user_role import UserRole
from src.exceptions import FieldAlreadyInUseError


class RegisterUser:
    def __init__(self, user: User, role: UserRole):
        self.__user = user
        self.__role = role
        self.__user.is_superuser = self.__role == UserRole.ADMIN
        self.__database_interface = SQLLiteInterface()

    def create_model(self):
        """Creates an instance of UserModel based on the User entity provided

        Returns
        -------
        UserModel
            The UserModel created based on the User entity provided
        """
        return UserModel.from_entity(self.__user)

    def register_user(self, user_entity: User):
        used_spot = (
            len(
                self.__database_interface.where(
                    model_class=UserModel,
                    condition=(
                        (UserModel.email == user_entity.email)
                        | (UserModel.username == user_entity.username)
                    ),
                )
            )
            > 0
        )

        if not used_spot:
            user_model = self.create_model()
            self.__database_interface.create(user_model)
            return user_model
        else:
            raise FieldAlreadyInUseError(field="Email or username")
