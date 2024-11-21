from .abstract_user import AbstractUser

class ClientUser(AbstractUser):
    """
    The ClientUser class is a class that defines the basic structure and behaviour of a client user.
    """
    def __init__(self, *args, **kwargs):
        """Class Constructor"""
        super().__init__(*args, **kwargs)