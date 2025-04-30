# server/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.auth import router as auth_router

app = FastAPI()

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

# Include the API routes from the `api` module
app.include_router(auth_router)