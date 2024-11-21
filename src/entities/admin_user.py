from .abstract_user import AbstractUser

class AdminUser(AbstractUser):
    """
    The AdminUser class is a class that defines the basic structure and behaviour of an admin user.
    """
    def __init__(self, *args, **kwargs):
        """Class Constructor"""
        super().__init__(*args, **kwargs)