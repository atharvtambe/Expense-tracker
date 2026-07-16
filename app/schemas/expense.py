from datetime import date
from pydantic import BaseModel

class ExpenseCreate(BaseModel):
    title: str
    description: str
    amount: float
    date: date
    category_id: int


class ExpenseResponse(BaseModel):
    id: int
    title: str
    description: str
    amount: float
    date: date
    category_id: int
    user_id: int

    class Config:
        from_attributes = True