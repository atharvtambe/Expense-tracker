from pydantic import BaseModel
from datetime import date

class ExpenseBase(BaseModel):
    title: str
    description: str
    amount: float
    date: date
    category_id: int


class ExpenseCreate(ExpenseBase):
    pass


class ExpenseUpdate(ExpenseBase):
    pass


class ExpenseResponse(ExpenseBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True