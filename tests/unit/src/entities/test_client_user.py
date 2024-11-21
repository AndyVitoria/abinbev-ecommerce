from src.entities.client_user import ClientUser
from .test_abstract_user import AbstractUserTest

class ClientUserTest(AbstractUserTest):
    user_class = ClientUser