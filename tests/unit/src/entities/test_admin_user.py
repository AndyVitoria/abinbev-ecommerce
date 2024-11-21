from src.entities.admin_user import AdminUser
from .test_abstract_user import AbstractUserTest

class AdminUserTest(AbstractUserTest):
    user_class = AdminUser
    