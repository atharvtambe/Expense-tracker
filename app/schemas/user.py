from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    phone_number:str
        
class UserUpdate(BaseModel):
    username: str
    email: EmailStr
    phone_number: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    created_at: datetime
    
class ChangePassword(BaseModel):
    old_password: str
    new_password: str

    class Config:
        from_attributes = True
        
