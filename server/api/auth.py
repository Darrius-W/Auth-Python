# server/api/auth.py

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

# Contact form data model
class LoginData(BaseModel):
    username: str
    password: str

# Get Login data
@router.post('/authLogin')
async def login(data: LoginData):
    print("Username: %s\nPassword: %s" % (data.username, data.password))