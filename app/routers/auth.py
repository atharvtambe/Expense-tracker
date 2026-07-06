from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

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