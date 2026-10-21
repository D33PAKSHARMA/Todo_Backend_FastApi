import re
from pydantic import EmailStr, field_validator
from sqlmodel import SQLModel, Field

class UserBase(SQLModel):
    name: str=Field(max_length=50)
    email: str = Field(unique=True, index=True)


class User(UserBase, table=True): # db table
    id: int | None = Field(default=None, primary_key=True)
    hashed_pass: str
    
# you can create a saparate schema file for req,res body

class UserReq(UserBase): # request body
    email: EmailStr
    password: str = Field(min_length=6, max_length=64)
    
    @field_validator('email')
    @classmethod
    def validate_email(cls, v: str)-> str:
        return v.strip().lower()

class UserReqLogin(SQLModel):
    email: str
    password: str

class UserResLogin(SQLModel):
    token: str
    message: str
        
    
class UserResponse(UserBase): # res body
    id: int