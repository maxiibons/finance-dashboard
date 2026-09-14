from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
import os

# Falls back to local URL if environment variable isn't set
DATABASE_URL = os.getenv(
    "DATABASE_URL", "postgresql://postgres:secretpassword@localhost:5432/financedb")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session maker for database transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    # Base class for your ORM models to inherit from
    pass

# Dependency to get the database session in your FastAPI paths


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
