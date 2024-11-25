from unittest import TestCase
from pydantic import ValidationError
import pytest
from src.entities.users.user import User


class BaseUserTest(TestCase):
    user_class = User

    def generate_client_user(
        self,
        username="john",
        password="Pa$$1234",
        email="john@mail.com",
        is_superuser=False,
    ):
        return self.user_class(
            username=username, password=password, email=email, is_superuser=is_superuser
        )

    def test_user_client(self):
        self.generate_client_user()

    def test_invalid_username_none(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(username=None)

    def test_invalid_username_empty(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(username="")

    def test_invalid_username_type(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(username=123)

    def test_invalid_username_type(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(username=123)

    def test_invalid_username_starting_with_number(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(username="1john")

    def test_invalid_username_with_special_character(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(username="@john")
        with pytest.raises(ValidationError):
            self.generate_client_user(username="j@hn")

    def test_invalid_username_longer_than_20_characters(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(username="abc" * 7)

    def test_invalid_password_none(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(password=None)

    def test_invalid_password_empty(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(password="")

    def test_invalid_password_type(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(password=123)

    def test_invalid_password_shorter_than_8_characters(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(password="Pa$$123")

    def test_invalid_password_no_uppercase(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(password="pa$$1234")

    def test_invalid_password_no_lowercase(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(password="PA$$1234")

    def test_invalid_password_no_number(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(password="Pa$$abcd")

    def test_invalid_password_no_special_character(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(password="Pass1234")

    def test_invalid_email_none(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(email=None)

    def test_invalid_email_empty(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(email="")

    def test_invalid_email_type(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(email=123)

    def test_invalid_email_format(self):
        with pytest.raises(ValidationError):
            self.generate_client_user(email="johnmail.com")
        with pytest.raises(ValidationError):
            self.generate_client_user(email="john@mailcom")
        with pytest.raises(ValidationError):
            self.generate_client_user(email="johnmailcom")

    def test_invalid_password_contains_username(self):
        with pytest.raises(ValueError):
            self.generate_client_user(username="john", password="johnPa$$1234")

    def test_create_user(self):
        username = "jhonwick"
        password = "Pa$$1234"
        email = "john@wick.com"
        is_superuser = True

        user = self.generate_client_user(
            username=username, password=password, email=email, is_superuser=is_superuser
        )

        assert user.username == username
        assert user.password.get_secret_value() == password
        assert user.email == email
        assert user.is_superuser == is_superuser