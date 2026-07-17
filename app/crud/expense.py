from sqlalchemy.orm import Session
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate


def create_expense(db: Session, expense: ExpenseCreate, user_id: int):
    new_expense = Expense(
        title=expense.title,
        description=expense.description,
        amount=expense.amount,
        date=expense.date,
        category_id=expense.category_id,
        user_id=user_id
    )

    db.add(new_expense)
    db.commit()
    db.refresh(new_expense)

    return new_expense


def get_expenses(db: Session, user_id: int):
    return (
        db.query(Expense)
        .filter(Expense.user_id == user_id)
        .all()
    )
    
def update_expense(db, expense_id, expense_data, user_id):
    expense = (
        db.query(Expense)
        .filter(
            Expense.id == expense_id,
            Expense.user_id == user_id
        )
        .first()
    )

    if not expense:
        return None

    expense.title = expense_data.title
    expense.description = expense_data.description
    expense.amount = expense_data.amount
    expense.date = expense_data.date
    expense.category_id = expense_data.category_id

    db.commit()
    db.refresh(expense)

    return expense

def delete_expense(db, expense_id, user_id):
    expense = (
        db.query(Expense)
        .filter(
            Expense.id == expense_id,
            Expense.user_id == user_id
        )
        .first()
    )

    if not expense:
        return None

    db.delete(expense)
    db.commit()

    return {"message": "Expense deleted successfully"}

def update_expense(db, expense_id, expense_data, user_id):
    expense = (
        db.query(Expense)
        .filter(
            Expense.id == expense_id,
            Expense.user_id == user_id
        )
        .first()
    )

    if not expense:
        return None

    expense.title = expense_data.title
    expense.description = expense_data.description
    expense.amount = expense_data.amount
    expense.date = expense_data.date
    expense.category_id = expense_data.category_id

    db.commit()
    db.refresh(expense)

    return expense