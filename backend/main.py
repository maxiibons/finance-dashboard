from db.database import engine, get_db
from crud import crud
from db import models, schemas
from typing import List
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware


# Automatically create database tables if they don't exist yet
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Finance Dashboard API")

# Ensure this middleware is added before your routers/endpoints
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://*.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],  # Must allow OPTIONS/all methods
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "Finance dashboard backend is running!"}


@app.get("/transactions/", response_model=List[schemas.TransactionResponse])
def read_transactions(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    transactions = crud.get_transactions(db, skip=skip, limit=limit)
    return transactions


@app.post("/transactions/", response_model=schemas.TransactionResponse)
def create_transaction(transaction: schemas.TransactionCreate, db: Session = Depends(get_db)):
    return crud.create_transaction(db=db, transaction=transaction)
