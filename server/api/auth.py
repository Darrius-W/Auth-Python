# server/api/auth.py

from fastapi import APIRouter
from schemas.auth import LoginData
from utils.security import hash_password

router = APIRouter()

# Get Login data
@router.post('/authLogin')
async def login(data: LoginData):
    hashed_password = hash_password(data.password)
    print("Username: %s\nPassword: %s" % (data.username, hashed_password))