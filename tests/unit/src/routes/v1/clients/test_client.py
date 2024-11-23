from fastapi.testclient import TestClient

from src.routes.v1.clients import client_router

client = TestClient(client_router)

def get_client_json(username: str = "TestClient", email: str = "test@client.com", password: str = "T3stP4ssw@rd"):
    return {
        "username": username,
        "email": email,
        "password": password
    }

def test_read_clients():
    body = get_client_json()
    response = client.post("/clients", json=body)
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}


# def test_read_clients_invalid_username():
#     invalid_input = {
#         "1TestClient": 422, # Starting with number
#         #1234: 422, # Invalid type
#         #"@TestClient": 422, # Special character
#         #"TestClient"*7: 422, # Longer than 20 characters
#         #"": 422, # Empty
#         #None: 422 # None
#     }
#     for invalid_input, status_code in invalid_input.items():
#         body = get_client_json(username=invalid_input)
#         response = client.post("/clients", json=body)
#         assert response.status_code == status_code
#         assert response.json()[0]["input"] == invalid_input