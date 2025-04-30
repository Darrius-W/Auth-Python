from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Contact form data model
class LoginData(BaseModel):
    userName: str
    userPass: str

# All domains to allow CORS
origins = [
    "http://localhost:3000",
    "http://localhost:8000/",
    "http://localhost:8000/authLogin"
    "http://localhost:8000/Signup"
]

# Middleware configuration for Cross-Origin Resource Sharing
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST", "GET"],
    allow_headers=["Content-Type"],
)

# Get Login data
@app.post('/authLogin')
async def login(userName: str = Form(...), userPass: str = Form(...)):
    print("here")
    #user = LoginData(userName=username, userPass=password)
    print("Username: %s\nPassword: %s" % (userName, userPass))