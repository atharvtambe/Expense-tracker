from fastapi import APIRouter, Depends
from app.dependencies import get_current_user

router = APIRouter()

@router.get("/dashboard")
def dashboard(current_user: str = Depends(get_current_user)):
    return {
        "message": "Welcome",
        "user": current_user
    }