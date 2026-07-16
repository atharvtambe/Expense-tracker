from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user

from app.crud.expense import create_expense, get_expenses

from app.schemas.expense import ExpenseCreate

from app.models.user import User

router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)

@router.post("/")
def add_expense(
    expense: ExpenseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_expense(
        db,
        expense,
        current_user.id
    )
    
    
@router.get("/")
def list_expenses(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_expenses(
        db,
        current_user.id
    )
    
    
@router.get("/")
def list_expenses(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_expenses(
        db,
        current_user.id
    )
