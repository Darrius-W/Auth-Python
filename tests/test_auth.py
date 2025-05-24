from fastapi.testclient import TestClient
from server.main import app
from server.db.database import user_hash_table

client = TestClient(app)

# Testing signup success with valid credentials and received token
def test_signup_success():
    response = client.post("/addUser", json={
        "username": "testuser",
        "password": "testpassword",
        "passwordConfirm": "testpassword"
    })
    
    assert response.status_code == 200
    assert "access_token" in response.json()
    
# Testing signup failure - Reason: Mismatched passwords
def test_signup_password_mismatch():
    response = client.post("/addUser", json={
        "username": "baduser",
        "password": "baddata123",
        "passwordConfirm": "baddata234"
    })
    
    assert response.status_code == 400
    assert response.json()["detail"] == "Passwords do not match"

# Testing signup failure - Reason: Username already exists
def test_signup_username_taken():
    response = client.post("/addUser", json={
        "username": "testuser",
        "password": "testpassword",
        "passwordConfirm": "testpassword"
    })
    
    assert response.status_code == 409
    assert response.json()["detail"] == "Username Taken"
    
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
    
# Testing login failure - Reason: non-existent user
def test_login_nonexistent_user():
    response = client.post("/login", json={
        "username": "notauser",
        "password": "notapassword"
    })
    
    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid Credentials"
    assert "access_token" not in response.cookies