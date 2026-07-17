from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.category import CategoryCreate
from app.crud.category import create_category, delete_category, get_categories, get_category, update_category
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

@router.get("/{category_id}")
def get_single_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    category = get_category(db, category_id)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category

@router.put("/{category_id}")
def edit_category(
    category_id: int,
    name: str,
    db: Session = Depends(get_db)
):
    category = update_category(db, category_id, name)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    return category

@router.delete("/{category_id}")
def remove_category(
    category_id: int,
    db: Session = Depends(get_db)
):
    success = delete_category(db, category_id)

    if not success:
        raise HTTPException(status_code=404, detail="Category not found")

    return {"message": "Category deleted successfully"}