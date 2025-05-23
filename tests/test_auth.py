from fastapi.testclient import TestClient
from server.main import app
from server.db.database import user_hash_table

client = TestClient(app)

# Tests that a user can sign up with valid credentials and receives token in response
def test_signup_success():
    response = client.post("/addUser", json={
        "username": "testuser",
        "password": "testpassword",
        "passwordConfirm": "testpassword"
    })
    
    assert response.status_code == 200
    assert "access_token" in response.json()
    
# Tests that server rejects users with mismatched passwords
def test_signup_password_mismatch():
    response = client.post("/addUser", json={
        "username": "baduser",
        "password": "baddata123",
        "passwordConfirm": "baddata234"
    })
    
    assert response.status_code == 400
    assert response.json()["detail"] == "Passwords do not match"