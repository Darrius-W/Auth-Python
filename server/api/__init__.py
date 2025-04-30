# server/api/__init__.py

from fastapi import APIRouter
from api.auth import router as auth_router

api_router = APIRouter()

# Include the auth routes into the main API router
api_router.include_router(auth_router, prefix="/auth", tags=["auth"])
