from app.auth import get_current_user
from fastapi import Depends, HTTPException

def get_current_user_id(userdata =  Depends(get_current_user)):
    if not userdata:
        raise HTTPException(status_code=401, detail="User not found")
    return int(userdata.id)

