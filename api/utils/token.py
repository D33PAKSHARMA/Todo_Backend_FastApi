import jwt
import os
from api.config.config import settings

key = settings.secret_key
algo = settings.algorithm
print(">><", key,algo)
def create_token(data)-> str:
    to_encode = data.copy()
    token = jwt.encode(to_encode, key, algorithm=algo)
    return token
    