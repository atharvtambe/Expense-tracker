from sqlalchemy.orm import Session
from app.models.expense import Expense
from app.schemas.expense import ExpenseCreate

from sqlalchemy.orm import Session
from app.models.expense import Expense


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


from sqlalchemy import desc

def get_expenses(
    db,
    user_id,
    category_id=None,
    min_amount=None,
    max_amount=None,
    search=None,
    sort_by=None,
    order="asc",
    page=1,
    limit=10,
):
    query = db.query(Expense).filter(
        Expense.user_id == user_id
    )

    # Category Filter
    if category_id:
        query = query.filter(
            Expense.category_id == category_id
        )

    # Amount Filters
    if min_amount is not None:
        query = query.filter(
            Expense.amount >= min_amount
        )

    if max_amount is not None:
        query = query.filter(
            Expense.amount <= max_amount
        )

    # Search
    if search:
        query = query.filter(
            Expense.title.ilike(f"%{search}%")
        )

    # -----------------------------
    # SORTING (Add here)
    # -----------------------------
    if sort_by == "amount":
        if order == "desc":
            query = query.order_by(desc(Expense.amount))
        else:
            query = query.order_by(Expense.amount)

    elif sort_by == "date":
        if order == "desc":
            query = query.order_by(desc(Expense.date))
        else:
            query = query.order_by(Expense.date)

    # -----------------------------
    # PAGINATION
    # -----------------------------
    offset = (page - 1) * limit

    query = query.offset(offset).limit(limit)

    return query.all()
    
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



def get_expenses(
    db: Session,
    user_id: int,
    category_id: int = None,
    min_amount: float = None,
    max_amount: float = None,
):

    query = db.query(Expense).filter(
        Expense.user_id == user_id
    )

    if category_id:
        query = query.filter(
            Expense.category_id == category_id
        )

    if min_amount is not None:
        query = query.filter(
            Expense.amount >= min_amount
        )

    if max_amount is not None:
        query = query.filter(
            Expense.amount <= max_amount
        )

    return query.all()