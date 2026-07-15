from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.category import CategoryCreate
from app.crud.category import create_category, get_categories
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)

@router.post("/")
def add_category(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return create_category(db, category.name)


@router.get("/")
def list_categories(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return get_categories(db)