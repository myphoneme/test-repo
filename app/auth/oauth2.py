from fastapi.security import OAuth2PasswordBearer 
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from jose import JWTError, jwt
from app.models import User

oauth2 = OAuth2PasswordBearer(tokenUrl = "/login")

ALGORITHM = "HS256"
SECRET_KEY = "abcd-1234-efgh-5678"



def get_current_user(token : str = Depends(oauth2), db:Session = Depends(get_db)):
    try:
        payload = jwt.decode(token , SECRET_KEY, algorithms= [ALGORITHM] )
        user_id = payload.get('sub')
        if not user_id:
            raise HTTPException(status_code=401, detail= "Invalid Token")
        user = db.query(User).filter(User.id == int(user_id)).first()
        if not user:
            raise HTTPException(status_code= 401, detail= "User not found")
        return user
    except JWTError:
        raise HTTPException(status_code= 401, detail= "Token verification failed")

        



