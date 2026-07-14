from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates

from app.auth import create_access_token
from app.dependencies import get_db
from app.models.user import User
from app.schemas.auth import Login
from app.utils.security import verify_password
from sqlalchemy.orm import Session

router = APIRouter()

templates = Jinja2Templates(directory="app/templates")


@router.get("/login")
def login(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="login.html"
    )

@router.get("/register")
def register(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="register.html"
    )
    
    
@router.post("/login")
def login(
    user: Login,
    db: Session = Depends(get_db)
):

    db_user = db.query(User).filter(
        User.email == user.email
    ).first()

    if not db_user:
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    if not verify_password(
        user.password,
        db_user.hashed_password
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Credentials"
        )

    token = create_access_token(
        {"sub": db_user.email}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }