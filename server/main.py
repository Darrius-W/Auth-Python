# server/main.py

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db.database import user_hash_table#, SessionLocal, engine, Base, get_db
from models.models import User
from pydantic import BaseModel
from utils.security import hash_password, verify_password

class NewUserData(BaseModel):
    username: str
    password: str
    passwordConfirm: str

class UserLoginData(BaseModel):
    username: str
    password: str

app = FastAPI()

# Create tables if they dont exist
#Base.metadata.create_all(bind=engine)

# All domains to allow CORS
origins = [
    "http://localhost:3000",
    "http://localhost:8000/",
    "http://localhost:8000/addUser"
]

# Middleware configuration for Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["Content-Type"],
)

# Validate User
@app.post('/login')
async def validateUser(data: UserLoginData):
    if data.username in user_hash_table:
        if verify_password(data.password, user_hash_table[data.username]):
            print("Valid user")
    else:
        raise HTTPException(status_code=401, details="Invalid Credentials")

# Create new user
@app.post('/addUser')
async def addUser(data: NewUserData):#, db: Session = Depends(get_db)):
    # Verify that passwords match
    if data.password != data.passwordConfirm:
        raise HTTPException(status_code=400, detail="Passwords do not match")
    
    new_user = User(
        username = data.username,
        hashed_password = hash_password(data.password)
    )
    user_hash_table.update({new_user.username: new_user.hashed_password})# Adding user to temporary user DB/Hash table
    '''
    # Adding user to PostgreSQL DB
    db.add(new_user)
    db.commit()
    db.refresh(new_user) # Get the ID and new data
    '''
    print(user_hash_table)
    return {"id": new_user.id, "username": new_user.username}