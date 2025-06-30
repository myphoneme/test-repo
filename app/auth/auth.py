from fastapi import Depends, HTTPException,APIRouter
from app.database import get_db
from app.models import User
from app.schemas import UserLogin
from sqlalchemy.orm import Session
from app.auth.jwt_handler import create_access_token
router = APIRouter()

@router.post("/login")
def login(userdata: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(userdata.email == User.email).first()
    if not user or userdata.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid Credential ")
    payload = {"sub": str(user.id), "name" : user.name}
    token = create_access_token(payload)
    return {"access_token": token , "token-type" : "bearer"}
