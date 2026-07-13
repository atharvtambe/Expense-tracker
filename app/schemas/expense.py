from pydantic import BaseModel
from datetime import date


class ExpenseCreate(BaseModel):
    amount: float
    description: str
    date: date
    category_id: int


class ExpenseResponse(BaseModel):
    id: int
    amount: float
    description: str
    date: date
    category_id: int
    user_id: int

    class Config:
        from_attributes = True