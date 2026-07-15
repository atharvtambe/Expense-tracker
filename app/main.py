from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.config import settings
from app.routers import home
from app.routers import auth
from app.routers import contact,register,user,category
from app.database import Base, engine

import app.models

from sqlalchemy import text
from app.database import engine

app = FastAPI(title="Expense Tracker")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(home.router)
app.include_router(auth.router)
app.include_router(contact.router)
app.include_router(register.router)
app.include_router(user.router)
app.include_router(category.router)



print(settings.DATABASE_URL)

@app.get("/db-test")
def db_test():

    with engine.connect() as connection:

        result = connection.execute(text("SELECT version();"))

        return {
            "database": result.scalar()
        }
        
        
