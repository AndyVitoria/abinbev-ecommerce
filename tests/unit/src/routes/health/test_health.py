from fastapi.testclient import TestClient
from src.routes.health import health_router


def test_read_health_fail():
    client = TestClient(health_router)
    response = client.post("/health")
    assert response.status_code == 405


def test_read_health():
    client = TestClient(health_router)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
