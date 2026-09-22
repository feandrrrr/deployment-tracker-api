from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "Deployment Tracker API is running"
    }


def test_create_deployment():
    response = client.post(
        "/deployments",
        json={
            "id": 100,
            "service_name": "test-service",
            "environment": "development",
            "version": "1.0.0",
            "status": "planned",
            "owner": "Test User",
            "risk_level": "low"
        }
    )

    assert response.status_code == 200
    assert response.json()["service_name"] == "test-service"


def test_invalid_deployment():
    response = client.post(
        "/deployments",
        json={
            "id": 101,
            "service_name": "broken-service",
            "environment": "moon",
            "version": "1.0.0",
            "status": "banana",
            "owner": "Test User",
            "risk_level": "extreme"
        }
    )

    assert response.status_code == 422