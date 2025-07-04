from sqlalchemy import Column, Integer, String, Float
from database import Base

class Product(Base):
    """
    SQLAIchemy model for stroing product information in the database.
    """
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    category = Column(String)
