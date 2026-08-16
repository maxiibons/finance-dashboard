# schemas.py
from typing import Optional
from pydantic import BaseModel, Field

class TransactionCreate(BaseModel):
    """! Blueprint for validating data extracted from AMEX email"""
    description: str = Field(..., description="The merchant name extracted from the email")
    amount: float = Field(..., description="The dollar amount spent")
    date: str = Field(..., description="YYYY-MM-DD formatted string of the transaction date")

class TransactionRespone(TransactionCreate):
    """! Blueprint for sending transaction data out to the frontend"""
    id: int

    class Config:
        from_attributes=True # Tells pydantic to cleanly read data from SQLAlchemy objects


class BudgetCategoryCreate(BaseModel):
    """Blueprint for creating or updating a monthly category budget limit."""
    category_name: str = Field(..., description="e.g., Groceries, Dining Out, Transport")
    monthly_limit: float = Field(..., description="The maximum dollar amount allocated for the month")

class BudgetCategoryResponse(BudgetCategoryCreate):
    class Config:
        from_attributes = True


class CategoryBudgetStatus(BaseModel):
    """The calculated financial status for a single category."""
    limit: float = Field(..., description="The set budget limit")
    spent: float = Field(..., description="Total money spent this month")
    remaining: float = Field(..., description="Money left to spend (stops at 0)")
    is_over: bool = Field(..., description="True if spent exceeds limit")
    over_by: float = Field(..., description="How much money you went over budget")

class DashboardOverviewResponse(BaseModel):
    """The final payload sent to the UI to render all budget progress bars."""
    budgets: dict[str, CategoryBudgetStatus]