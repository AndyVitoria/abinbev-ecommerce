import pytest
from src.entities.client_user import ClientUser

def generate_client_user(username="john", password="pass123", email="john@mail.com"):
    return ClientUser(username=username, password=password, email=email)

def test_user_client():
    generate_client_user()

def test_invalid_username_none():
    with pytest.raises(TypeError):
        generate_client_user(username=None)

def test_invalid_username_empty():
    with pytest.raises(ValueError):
        generate_client_user(username="")

def test_invalid_username_type():
    with pytest.raises(TypeError):
        generate_client_user(username=123)

def test_invalid_username_type():
    with pytest.raises(TypeError):
        generate_client_user(username=123)

def test_invalid_username_starting_with_number():
    with pytest.raises(ValueError):
        generate_client_user(username="1john")