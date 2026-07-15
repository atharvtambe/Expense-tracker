from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.templating import Jinja2Templates

from app.auth import create_access_token
from app.crud.user import get_user_by_email
from app.database import get_db
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
    
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends

@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    user = get_user_by_email(db, form_data.username)

    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    if not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = create_access_token(
        {"sub": user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }