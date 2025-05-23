# Creates a database session

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#DATABASE_URL = "" # Link to PostgreSQL DB
user_hash_table = {} # User temporary DB

'''
# Create the engine
engine = create_engine(DATABASE_URL)
# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
'''
# Base class for models
Base = declarative_base()
'''
# Dependency function for FastAPI
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
'''