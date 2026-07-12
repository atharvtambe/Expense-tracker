from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String(50),
        nullable=False
    )

    color = Column(
        String(20),
        default="#4CAF50"
    )

    expenses = relationship(
        "Expense",
        back_populates="category"
    )