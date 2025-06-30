from sqlalchemy.orm import Session
from fastapi import Depends , APIRouter, HTTPException
from app.database import get_db
from app.schemas import CreateUser, UserResponse, UpdateUser
from app.crud import insertUser, get_all_user, get_user_by_id, update_user_user_id, delete_user_by_id, user_soft_delete
from app.models import User

router = APIRouter(prefix="/users", tags=["Users Section"])

@router.post("/create/", response_model=UserResponse)
def create_user(userdata : CreateUser,db:Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == userdata.email).first()
    if existing:
        raise HTTPException (status_code=400, detail= "Email already Exist")

    newUser = insertUser(db,userdata)
    return newUser
   
     
@router.get('/all', response_model= list[UserResponse])
def get_users(db:Session = Depends(get_db)):
    users = get_all_user(db)
    if not users:
        HTTPException(status_code=404, detail="User not found")
    return users 



@router.get('/{id}', response_model = UserResponse)
def user_by_id(id: int , db: Session = Depends(get_db)):
    user = get_user_by_id(db,id)
    if not user:
        # return {"message" : "User not found"}
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.put('/update/{id}', response_model= UserResponse)
def update_user(id: int, userdata : UpdateUser, db:Session = Depends(get_db) ):
    user = update_user_user_id(db, id, userdata)
    if not user:
        raise HTTPException(status_code=404, detail= "User not found")
    return user

@router.delete("/{id}")
def delete_user(id:int, db:Session = Depends(get_db)):
    user = delete_user_by_id(db,id)
    if not user:
        return {"message": "User Not Found"}
    return {"message" : "User deleted successfully"}

@router.delete("/delete/{id}")
def deleteUser(id: int, db: Session = Depends(get_db)): 
    user = user_soft_delete(db , id)
    if not user:
        return {"message" : "User not found"}
    return {"message" : "User Deleted Successfully !"}
