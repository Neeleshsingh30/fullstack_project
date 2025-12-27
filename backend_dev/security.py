# from datetime import datetime, timedelta
# from typing import Optional
# from jose import jwt, JWTError
# from fastapi import Depends, HTTPException, status
# from fastapi.security import OAuth2PasswordBearer

# # ================================
# # JWT CONFIG
# # ================================
# SECRET_KEY = "mysecretkey"  # later move to env variable
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

# # ✅ FIXED: absolute path
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


# # ================================
# # CREATE ACCESS TOKEN
# # ================================
# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
#     to_encode = data.copy()

#     expire = datetime.utcnow() + (
#         expires_delta
#         if expires_delta
#         else timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     )

#     to_encode.update({"exp": expire})

#     encoded_jwt = jwt.encode(
#         to_encode,
#         SECRET_KEY,
#         algorithm=ALGORITHM
#     )
#     return encoded_jwt


# # ================================
# # VERIFY & GET CURRENT USER
# # ================================
# def get_current_user(token: str = Depends(oauth2_scheme)) -> str:
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail="Could not validate credentials",
#         headers={"WWW-Authenticate": "Bearer"},
#     )

#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         email: Optional[str] = payload.get("sub")

#         if email is None:
#             raise credentials_exception

#         return email

#     except JWTError:
#         raise credentials_exception







from datetime import datetime, timedelta
from typing import Optional
from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

SECRET_KEY = "mysecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if email is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return email
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
