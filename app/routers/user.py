from fastapi import APIRouter, Depends
from app.crud.user import change_password, delete_user, update_user
from app.database import get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.schemas.user import ChangePassword, UserUpdate
from sqlalchemy.orm import Session


router = APIRouter(tags=["User"])


@router.get("/me")
def get_me(current_user: str = Depends(get_current_user)):
    return {
        "message": "Welcome",
        "email": current_user
    }
    
@router.put("/me", response_model=UserUpdate)
def update_profile(
    user: UserUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return update_user(db, current_user.id, user)

@router.put("/change-password")
def update_password(
    data: ChangePassword,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return change_password(db, current_user.id, data)

@router.delete("/me")
def delete_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return delete_user(db, current_user.id)