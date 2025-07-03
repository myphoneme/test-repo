from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.schemas import CategoryCreate, CategoryResponse, CategoryUpdate
from app.models import Category
from app.helper import get_current_user_id



def insertCategory(db: Session, data : CategoryCreate):
    cat = Category( name = data.name , description = data.description, created_by = get_current_user_id )
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat 

