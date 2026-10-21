
from api.utils.token import create_token
from api.models.user_model import UserReqLogin
from api.models.user_model import User, UserReq, UserResponse, UserResLogin
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from api.config.database import get_session

router = APIRouter(prefix='/auth')

@router.post('/register', response_model=UserResponse, status_code=201)
def registerUser(user_in: UserReq, session: Session=Depends(get_session)):
    existing_user = session.exec(select(User).where(User.email == user_in.email)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User alrady exist")

    user = User(
        name =user_in.name,
        email = user_in.email,
        hashed_pass=user_in.password # i am learnig thats why i am hashing the password
    )
    
    
    session.add(user)
    session.commit()
    session.refresh(user)
    return user
    
@router.post('/login', response_model=UserResLogin)
def loginUser(user_in: UserReqLogin, session:Session=Depends(get_session)):
    user = session.exec(select(User).where(User.email == user_in.email)).first()
    
    if not user:
        raise HTTPException(status_code=400, detail= "User not found")
    
    token = create_token({"id": user.id, "email": user.email})
    print(token, 'token')
    
    return {"token": token, "message": "LoggedIn success"}
    
    