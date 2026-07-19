from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.crud.user import create_user, get_user_by_email
from app.database import get_db
from app.schemas.user import UserCreate
from fastapi import status

router = APIRouter() 

@router.post("/register",status_code=status.HTTP_201_CREATED)
def register(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    existing = get_user_by_email(db, user.email)

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return create_user(db, user)