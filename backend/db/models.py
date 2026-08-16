# backend/db/models.py
from db.database import Base
from sqlalchemy import Float, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

class BudgetCategory(Base):
    """The master table for your custom category buckets and spending limits."""
    __tablename__ = "budget_categories"

    # We make category_name the primary key because every category must be completely unique
    category_name: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    monthly_limit: Mapped[float] = mapped_column(Float, nullable=False)

    # Relationship linking this category to any transactions tagged with it
    transactions: Mapped[list["Transaction"]] = relationship(
        "Transaction", back_populates="budget_category"
    )

class Transaction(Base):
    """The continuous ledger tracking every single card expense parsed from emails."""
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    date: Mapped[str] = mapped_column(String, nullable=False)  # Saved as "YYYY-MM-DD" text
    description: Mapped[str] = mapped_column(String, nullable=False) # e.g. "Woolworths Strathfield"
    amount: Mapped[float] = mapped_column(Float, nullable=False)

    # Links a transaction to a specific category. 
    # It can be nullable=True because new transactions will start as "Uncategorized" 
    category_name: Mapped[str | None] = mapped_column(
        String, ForeignKey("budget_categories.category_name"), nullable=True
    )

    # Connects back to the parent category object
    budget_category: Mapped[BudgetCategory | None] = relationship(
        "BudgetCategory", back_populates="transactions"
    )