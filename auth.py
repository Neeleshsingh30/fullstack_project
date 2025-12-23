# auth.py
from passlib.context import CryptContext

# bcrypt hashing config
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# password → hash
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# verify plain password with hash
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
