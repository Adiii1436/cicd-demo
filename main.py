from fastapi import FastAPI

app = FastAPI(
    title="FastAPI UV Demo",
    description="A simple FastAPI app using uv, Docker, and Docker Compose",
    version="1.0.0",
)


@app.get("/")
def home():
    return {
        "message": "FastAPI V2 app is running successfully"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": f"User {user_id}"
    }