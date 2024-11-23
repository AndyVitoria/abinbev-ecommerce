from pydantic import BaseModel, EmailStr, SecretStr, field_validator
import re

from .user_pattern import UserPatterns

class BaseUser(BaseModel):
    username: str
    password: SecretStr
    email: EmailStr

    @field_validator("password")
    def check_password(cls, value: SecretStr):
        print(value.get_secret_value())
        patterns = UserPatterns()
        if re.match(patterns.PASSWORD_PATTERN, value.get_secret_value()) is None:
            raise ValueError("Password must have at least 8 characters, one uppercase letter, one lowercase letter, one number, one special character.")
        return value
    
    @field_validator("username")
    def check_username(cls, value: str):
        patterns = UserPatterns()
        if re.match(patterns.USERNAME_PATTERN, value) is None:
            raise ValueError("Username must have between 4 and 20 characters and start with a letter.")
        return value
    
    def validate_user(self):
        """Validates the user's information."""
        if self.username in self.password.get_secret_value():
            raise ValueError("Password cannot contain the username on it.")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.validate_user()