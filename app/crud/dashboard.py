from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.expense import Expense
from sqlalchemy import extract
from app.models.category import Category


def total_expense(db: Session, user_id: int):
    total = (
        db.query(func.sum(Expense.amount))
        .filter(Expense.user_id == user_id)
        .scalar()
    )

    return {
        "total_expense": total or 0
    }
    


def monthly_expense(db, user_id):
    result = (
        db.query(
            extract("month", Expense.date).label("month"),
            func.sum(Expense.amount).label("total")
        )
        .filter(Expense.user_id == user_id)
        .group_by(extract("month", Expense.date))
        .order_by(extract("month", Expense.date))
        .all()
    )

    return [
        {
            "month": int(row.month),
            "total": float(row.total)
        }
        for row in result
    ]
    


def category_summary(db, user_id):
    result = (
        db.query(
            Category.name.label("category"),
            func.sum(Expense.amount).label("total")
        )
        .join(Expense, Expense.category_id == Category.id)
        .filter(Expense.user_id == user_id)
        .group_by(Category.name)
        .all()
    )

    return [
        {
            "category": row.category,
            "total": float(row.total)
        }
        for row in result
    ]