from fastapi.testclient import TestClient

from src.routes.v1.clients import client_router
from mock import patch


client = TestClient(client_router)


def get_client_json(
    username: str = "TestClient",
    email: str = "test@client.com",
    password: str = "T3stP4ssw@rd",
):
    return {"username": username, "email": email, "password": password}


def test_register_clients():
    body = get_client_json()
    with patch("src.usecases.RegisterUser.register_user") as mock_client_usecasse:
        mock_client_usecasse.post.return_value = True
        response = client.post("/clients", json=body)
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}
