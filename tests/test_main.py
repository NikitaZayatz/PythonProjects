from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    """Тест главной страницы"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello from CI/CD!"
    assert data["status"] == "running"

def test_health_check():
    """Тест эндпоинта здоровья"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_user():
    """Тест эндпоинта с пользователем"""
    response = client.get("/users/42")
    assert response.status_code == 200
    data = response.json()
    assert data["user_id"] == 42
    assert data["name"] == "User 42"