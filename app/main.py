from fastapi import FastAPI

app = FastAPI(title="My CI/CD App", version="1.0.0")

@app.get("/")
def root():
    """Главная страница"""
    return {"message": "Hello from CI/CD!", "status": "running"}

@app.get("/health")
def health_check():
    """Эндпоинт для проверки здоровья (используется Kubernetes)"""
    return {"status": "healthy"}

@app.get("/users/{user_id}")
def get_user(user_id: int):
    """Пример эндпоинта с параметром"""
    return {"user_id": user_id, "name": f"User {user_id}"}