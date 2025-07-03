from sqlalchemy import Column, Integer, String, DateTime
from .base import Base
from datetime import datetime
 

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(250), nullable= False)
    role  = Column(Integer, nullable=False, default=1)  # 1 for user, 2 for admin
    created_at = Column(DateTime(timezone=True), default=datetime.now)
    updated_at = Column(DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    deleted_at = Column(DateTime(timezone=True), nullable=True)
    is_active = Column(Integer, default=1)  # 1 for active, 0 for inactive
