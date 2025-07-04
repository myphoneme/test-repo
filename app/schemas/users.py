from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime
 

class UserBase(BaseModel):
    name : str 
    email: EmailStr
    

class CreateUser(UserBase):
    password : str


class UpdateUser(BaseModel):
    name : Optional[str]  = None
    email : Optional[EmailStr] = None
    password: Optional[str] = None

class UserResponse(UserBase):
    id: int
    created_at : datetime
     

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    email: EmailStr
    password : str