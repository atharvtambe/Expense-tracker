from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import home
from app.routers import auth
from app.routers import contact

app = FastAPI(title="Expense Tracker")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(home.router)
app.include_router(auth.router)
app.include_router(contact.router)