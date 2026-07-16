from sqlalchemy import Column, Integer, Float, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=False)

    description = Column(String)

    amount = Column(Float, nullable=False)

    date = Column(Date, nullable=False)

    category_id = Column(Integer, ForeignKey("categories.id"))

    user_id = Column(Integer, ForeignKey("users.id"))

    category = relationship("Category")

    owner = relationship("User", back_populates="expenses")