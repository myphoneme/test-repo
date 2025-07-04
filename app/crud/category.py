from sqlalchemy.orm import Session
from app.schemas import CategoryCreate, CategoryResponse, CategoryUpdate
from app.models import Category
 



def insertCategory(db: Session, data : CategoryCreate, user_id : int):
    cat = Category( name = data.name , description = data.description, created_by = user_id )
    db.add(cat)
    db.commit()
    db.refresh(cat)
    return cat 

