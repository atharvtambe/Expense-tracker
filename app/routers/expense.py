from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from typing import Optional
from app.crud.expense import create_expense, delete_expense, get_expenses, update_expense

from app.schemas.expense import ExpenseCreate, ExpenseResponse, ExpenseUpdate

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

@router.put("/{expense_id}")
def update(
    expense_id: int,
    expense: ExpenseUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    updated = update_expense(
        db,
        expense_id,
        expense,
        current_user.id
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return updated

@router.delete("/{expense_id}")
def delete(
    expense_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    deleted = delete_expense(
        db,
        expense_id,
        current_user.id
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Expense not found"
        )

    return deleted

@router.get("/", response_model=list[ExpenseResponse])
def list_expenses(
    category_id: Optional[int] = None,
    min_amount: Optional[float] = None,
    max_amount: Optional[float] = None,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_expenses(
        db=db,
        user_id=current_user.id,
        category_id=category_id,
        min_amount=min_amount,
        max_amount=max_amount,
    )
    
    
@router.get("/", response_model=list[ExpenseResponse])
def list_expenses(
    category_id: int | None = None,
    min_amount: float | None = None,
    max_amount: float | None = None,
    search: str | None = None,
    sort_by: str | None = None,
    order: str = "asc",
    page: int = 1,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return get_expenses(
        db=db,
        user_id=current_user.id,
        category_id=category_id,
        min_amount=min_amount,
        max_amount=max_amount,
        search=search,
        sort_by=sort_by,
        order=order,
        page=page,
        limit=limit,
    )