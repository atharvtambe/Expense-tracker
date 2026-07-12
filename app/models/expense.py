from sqlalchemy import (
    Column,
    Integer,
    Float,
    String,
    Date,
    ForeignKey
)

from sqlalchemy.orm import relationship

from app.database import Base


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    amount = Column(
        Float,
        nullable=False
    )

    description = Column(
        String(255)
    )

    date = Column(
        Date,
        nullable=False
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.id")
    )

    owner = relationship(
        "User",
        back_populates="expenses"
    )

    category = relationship(
        "Category",
        back_populates="expenses"
    )