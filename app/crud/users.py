from sqlalchemy.orm import Session
from app.models import User 
from app.schemas import CreateUser, UpdateUser


def insertUser(db: Session, userdata : CreateUser):
    newuser = User(name = userdata.name, email = userdata.email, password = userdata.password)
    db.add(newuser)
    db.commit()
    db.refresh(newuser)
    return newuser

def get_all_user(db:Session):
    return db.query(User).filter(User.is_active == 1).all()
     

def get_user_by_id(db: Session, userid : int):
    user = db.query(User).filter(User.is_active ==1 , User.id == userid).first()
    return user 


def update_user_user_id(db: Session, userid : int, userdata : UpdateUser ):
    user = db.query(User).filter(User.is_active ==1 , User.id == userid).first()
    if not user :
        return None
    if userdata.name is not None:
        user.name = userdata.name
    if userdata.email is not None:
        user.email = userdata.email
    if userdata.password is not None:
        user.password = userdata.password
    db.commit()
    db.refresh(user)
    return user 

    
def delete_user_by_id(db:Session, id: int):
    user = db.query(User).filter(User.is_active == 1, User.id == id).first()
    if not user :
        return None
    db.delete(user)
    db.commit()
    return user

def user_soft_delete(db:Session, id:int):
    user = db.query(User).filter(User.is_active == 1 , User.id == id).first()
    if not user:
        return None
    user.is_active = 0
    db.commit()
    return True
