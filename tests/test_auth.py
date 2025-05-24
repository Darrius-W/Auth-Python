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
    
# Testing successful login and ensuring token is received
def test_login_success():
    response = client.post("/login", json={
        "username": "testuser",
        "password": "testpassword"
    })
    
    assert response.status_code == 200
    assert response.json()["message"] == "Login Successful"
    assert "access_token" in response.cookies
    
# Testing login failure - Reason: wrong password
def test_login_wrong_password():
    response = client.post("/login", json={
        "username": "testuser",
        "password": "testp4ssword"
    })
    
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid Credentials"
    assert "access_token" not in response.cookies