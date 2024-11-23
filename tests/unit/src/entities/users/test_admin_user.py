from src.entities import AdminUser
from .test_base_user import BaseUserTest

class AdminUserTest(BaseUserTest):
    user_class = AdminUser