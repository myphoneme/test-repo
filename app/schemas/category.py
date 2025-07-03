from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CategoryBase(BaseModel):
    name: str 


class CategoryCreate(CategoryBase):
    description: Optional[str] = None
     
    

class CategoryResponse(CategoryCreate):
    id: int 
    created_by : int
    created_at : datetime
    updated_by : Optional[int]
    updated_at : Optional[datetime]

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    updated_by : int
