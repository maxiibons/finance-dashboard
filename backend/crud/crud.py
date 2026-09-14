from sqlalchemy.orm import Session
from db import models
from db import schemas


def get_transactions(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.TransactionModel).offset(skip).limit(limit).all()


def create_transaction(db: Session, transaction: schemas.TransactionCreate):
    db_transaction = models.TransactionModel(
        title=transaction.title,
        amount=transaction.amount,
        category=transaction.category
    )
    db.add(db_transaction)
    db.commit()
    db.refresh(db_transaction)
    return db_transaction
