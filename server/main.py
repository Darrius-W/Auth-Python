# server/main.py

from fastapi import FastAPI, HTTPException, Depends, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
#from sqlalchemy.orm import Session
from server.db.database import user_hash_table#, SessionLocal, engine, Base, get_db
from server.models.models import User
from pydantic import BaseModel
from server.utils.security import hash_password, verify_password, create_access_token, get_current_user

# Request model for signup
class NewUserData(BaseModel):
    username: str
    password: str
    passwordConfirm: str

# Request model for login
class UserLoginData(BaseModel):
    username: str
    password: str

app = FastAPI()

# Create tables if they dont exist
#Base.metadata.create_all(bind=engine)

# All domains to allow CORS
origins = [
    "http://localhost:3000"
    "http://localhost:8000/",
    "http://localhost:8000/addUser",
    "http://localhost:8000/login",
    "http://localhost:8000/protected",
    "http://localhost:8000/logout"
]

# Middleware configuration for Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["Content-Type"],
)

# Authenticates a user and sets an Http-only cookie with a JWT access token
@app.post('/login')
async def validateUser(data: UserLoginData):
    if data.username in user_hash_table:
        if verify_password(data.password, user_hash_table[data.username]):
            pass
        else:
            raise HTTPException(status_code=401, detail="Invalid Credentials")
    else:
        raise HTTPException(status_code=401, detail="Invalid Credentials")
    
    token = create_access_token({"sub": data.username})
    response = JSONResponse(content={"message": "Login Successful"})
    response.set_cookie(
        key = "access_token",
        value = token,
        httponly = True,
        secure = False, # True in production (HTTPS only)
        samesite = "Lax",
        max_age = 1800,
        path = "/"
    )
    return response

# Registers a new user and returns a token upon success
@app.post('/addUser')
async def addUser(data: NewUserData):#, db: Session = Depends(get_db)):
    # Verify that passwords match
    if data.password != data.passwordConfirm:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    
    if data.username in user_hash_table:
        raise HTTPException(status_code=409, detail="Username Taken")
    
    new_user = User(
        username = data.username,
        hashed_password = hash_password(data.password)
    )
    # Simulate adding user to a database using hash table for temporary storage
    user_hash_table.update({new_user.username: new_user.hashed_password})
    '''
    # Adding user to PostgreSQL DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user) # Get the ID and new data
    '''
    print(user_hash_table)
    token = create_access_token({"sub": new_user.username})
    return {"message": "Signup Successful", "access_token": token, "token_type": "bearer"}
    #return {"id": new_user.id, "username": new_user.username}

# Returns the current user if token is valid    
@app.get("/protected")
def protected_route(username: str = Depends(get_current_user)):
    print(username)
    return {"username": username["username"]}

# Clears access token and logs out user
@app.post("/logout")
def logout_user(response: Response):
    response.delete_cookie("access_token", path="/")
    return {"message": "Logged out successfully"}