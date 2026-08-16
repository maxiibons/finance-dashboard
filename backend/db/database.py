# backend/db/database.py
from core.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

# Create the engine.
# 'check_same_thread=False' is specific to SQLite so multiple async API requests can talk to it safely.
engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)  # Create a Session factory. Each time we talk to the DB, we will make a session from this.


# Dependency helper function that manages opening and closing the DB connection automatically
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Create the Base class. All our future database tables will inherit from this class.
class Base(DeclarativeBase):
    pass
