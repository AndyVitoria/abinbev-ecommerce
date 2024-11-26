from enum import Enum


class UserRole(str, Enum):
    ADMIN: str = 1
    CLIENT: str = 2
