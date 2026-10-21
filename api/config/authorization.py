from fastapi import Depends
from fastapi import HTTPException, Header
from sqlmodel import Session
from api.config.database import get_session
import jwt, os
from api.models.user_model import User
from api.config.config import settings


secret_key = settings.secret_key
algo = settings.algorithm
def authenticate(token: str= Header(None), session: Session= Depends(get_session)):
    if not token:
        raise HTTPException(
            status_code= 401,
            detail = "Token not found"
        )
        
    try:
        payload = jwt.decode(token, secret_key, algorithms=algo) 
        user_id = payload.get('id')
        if not user_id:
            raise HTTPException(
                status_code= 401,
                detail = "Unauthorize"
            )
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = session.get(User, user_id)
    if not user:
        raise HTTPException(
            status_code= 401,
            detail = "Unauthorize"
        )
    return user
        
            
                
    