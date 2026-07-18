from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate
from app.utils.security import hash_password, verify_password


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(
        User.email == email
    ).first()


def create_user(
    db: Session,
    user: UserCreate
):

    hashed = hash_password(user.password)

    db_user = User(
        username=user.username,
        email=user.email,
        hashed_password=hashed,
        phone_number = user.phone_number
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()

    db_user.username = user.username
    db_user.email = user.email
    db_user.phone_number = user.phone_number

    db.commit()
    db.refresh(db_user)

    return db_user

def change_password(db, user_id, data):
    user = db.query(User).filter(User.id == user_id).first()

    if not verify_password(data.old_password, user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    user.hashed_password = hash_password(data.new_password)

    db.commit()

    return {"message": "Password updated successfully"}

def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()

    db.delete(user)

    db.commit()

    return {"message": "User deleted successfully"}