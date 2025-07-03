from app.database import get_db
from fastapi import Depends , HTTPException, APIRouter
from sqlalchemy.orm import Session
from app.models import Category
from app.schemas import CategoryResponse, CategoryCreate
from app.crud import insertCategory
from app.auth import get_current_user
from app.helper import get_current_user_id

router = APIRouter(prefix="/category", tags=["Category Section"])

@router.post("/create", response_model= CategoryResponse)
def create_category(data : CategoryCreate, db : Session = Depends(get_db)):
    cat = db.query(Category).filter(Category.name == data.name, Category.is_active == 1).first()
    if cat:
        raise HTTPException(status_code=401, detail= "Category already exists !!")
    inserted_data = insertCategory(db, data)

    if not inserted_data:
        raise HTTPException(status_code=401, detail= "User can't be created !!")
    return inserted_data
    
@router.get("/userid")
def user_id(user = Depends(get_current_user)):
    if not user :
        raise HTTPException(status_code=401, detail="Use not found")
    return int(user.id)
 