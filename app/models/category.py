from .base import Base 
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(150), nullable=False, unique= True)   
    description = Column(String(500), nullable=True)   
    created_by = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now)

    updated_by = Column(Integer, nullable=True)   
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)

    is_active = Column(Integer, nullable=False, default=1)
