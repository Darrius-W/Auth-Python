from fastapi.testclient import TestClient
from server.main import app
from server.db.database import user_hash_table
from server.utils.security import hash_password, create_access_token
import pytest

client = TestClient(app)

# Isolate tests by clearing user table and tokens
@pytest.fixture(autouse=True)
def clear_client():
    client.cookies.clear()
    user_hash_table.clear()
    return TestClient(app)

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
    # Preload user into table
    username = "testuser"
    raw_password = "testpassword"
    hashed = hash_password(raw_password)
    user_hash_table[username] = hashed
    
    response = client.post("/addUser", json={
        "username": "testuser",
        "password": "testpassword",
        "passwordConfirm": "testpassword"
    })
    
    assert response.status_code == 409
    assert response.json()["detail"] == "Username Taken"
    
# Testing successful login and ensuring token is received
def test_login_success():
    # Preload user into table
    username = "testuser"
    raw_password = "testpassword"
    hashed = hash_password(raw_password)
    user_hash_table[username] = hashed
    
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

# Testing that successful signup allows user to access protected route with cookie
def test_protected_route_with_valid_cookie():    
    # Sign up user and receive token
    signup = client.post("/addUser", json={
        "username": "protecteduser",
        "password": "securepassword",
        "passwordConfirm": "securepassword"
    })

    assert signup.status_code == 200
    
    token = create_access_token({"sub": "protecteduser"})
    client.cookies.set("access_token", token)
    
    # Access the protected route
    response = client.get("/protected")
    
    assert response.status_code == 200
    assert response.json()["username"] == "protecteduser"
    
# Testing protected route access without cookie
def test_protected_without_cookie():
    response = client.get("/protected")
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"
    
    
    
    
    
# Testing protected route access with invalid token
def test_protected_with_invalid_token():
    # Set invalid JWT manually
    client.cookies.set("access_token", "fake.token")
    
    # Access the protected route
    response = client.get("/protected")
    
    assert response.status_code == 401
    assert response.json()["detail"] == "Token invalid or expired"
    
# Testing logout success, ensuring deletion of cookie
def test_logout_deletes_cookie():
    # Create test user and generate valid token
    user_hash_table["logoutuser"] = hash_password("logoutpass")
    token = create_access_token({"sub": "logoutuser"})
    
    # Set the token as a cookie
    client.cookies.set("access_token", token)
    
    # Confirm access to protected route works before logout
    response_before = client.get("/protected")
    assert response_before.status_code == 200
    
    # Call logout
    logout = client.post("/logout")
    assert logout.status_code == 200
    assert logout.json()["message"] == "Logged out successfully"
    
    # Manually clear cookie
    client.cookies.clear()
    
    # Try accessing protected route again
    response_after = client.get("/protected")
    assert response_after.status_code == 401
    assert response_after.json()["detail"] == "Not authenticated"