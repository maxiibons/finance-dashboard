from pydantic import BaseModel
from datetime import datetime

# Schema for creating a transaction (what the client sends)


class TransactionCreate(BaseModel):
    title: str
    amount: float
    category: str

# Schema for reading a transaction (what the API returns)


class TransactionResponse(TransactionCreate):
    id: int
    date: datetime

    class Config:
        from_attributes = True  # Allows Pydantic to read data from SQLAlchemy models
