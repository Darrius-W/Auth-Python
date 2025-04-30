# server/schemas/auth.py

from pydantic import BaseModel

# Contact form data model
class LoginData(BaseModel):
    username: str
    password: str