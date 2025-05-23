from fastapi.testclient import TestClient
from server.main import app
from server.db.database import user_hash_table

client = TestClient(app)

def test_signup_success():
    response = client.post("/addUser", json={
        "username": "testuser",
        "password": "testpassword",
        "passwordConfirm": "testpassword"
    })
    
    assert response.status_code == 200
    assert "access_token" in response.json()