    
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User

from app.crud.dashboard import (
    total_expense,
    monthly_expense,
    category_summary
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)

@router.get("/total-expense")
def get_total(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return total_expense(db, current_user.id)


@router.get("/monthly-expense")
def get_monthly(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return monthly_expense(db, current_user.id)


@router.get("/category-summary")
def get_category(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return category_summary(db, current_user.id)