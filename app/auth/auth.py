from fastapi import Depends, HTTPException,APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from app.database import get_db
from app.models import User
from app.schemas import UserLogin
from sqlalchemy.orm import Session
from app.auth.jwt_handler import create_access_token
from app.schemas import UserResponse
from .oauth2 import get_current_user
router = APIRouter()

@router.post("/login2")
def login2(userdata: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(userdata.email == User.email, User.is_active == 1).first()
    if not user or userdata.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid Credential ")
    payload = {"sub": str(user.id), "name" : user.name}
    token = create_access_token(payload)
    return {"access_token": token , "token-type" : "bearer"}


@router.post("/login")
def login(userdata: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(userdata.username == User.email).first()
    if not user or userdata.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid Credential ")
    payload = {"sub": str(user.id), "name" : user.name}
    token = create_access_token(payload)
    return {"access_token": token , "token-type" : "bearer"}

@router.get('/me', response_model= UserResponse)
def its_me(current_user = Depends(get_current_user)):
    return current_user