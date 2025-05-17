# server/utils/security.py

from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
import os
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status, Cookie

# Load environment variables from .env
load_dotenv()

# Secret key to sign and verify JWT tokens
SECRET_KEY = os.getenv("APP_SECRET_KEY")
# JWT algorithm
ALGORITHM = os.getenv("APP_ALGORITHM")
# Default token expiration (in minutes)
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Passlib context for password hashing using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 Bearer token scheme for use with Authorization header
# (used for endpoints expecting access tokens via headers)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Creates a JWT token with a payload and optional expiration time
def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire}) # Include expiration in payload
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# Decodes and validates JWT token sent via authorization header (bearer token)
def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload # Contains user info
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
        
# Hashes a plain-text password using bcrypt
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Verifies a plain password against its hash
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Retrieves the current user by decoding the JWT stored in an HTTP-only cookie
def get_current_user(access_token: str = Cookie(None)):
    if not access_token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    
    try:
        payload = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        return {"username": payload["sub"]}
    except JWTError:
        raise HTTPException(status_code=401, detail="Token invalid or expired")