from fastapi import APIRouter, Depends
from app.dependencies import get_current_user

router = APIRouter(tags=["User"])


@router.get("/me")
def get_me(current_user: str = Depends(get_current_user)):
    return {
        "message": "Welcome",
        "email": current_user
    }