from pydantic import BaseModel, ConfigDict
from typing import Optional, List


# -------------------- STUDENT SCHEMAS --------------------

class StudentCreate(BaseModel):
    name: str
    roll_no: str
    email: str
    department: Optional[str] = None
    year: Optional[int] = None
    phone: Optional[str] = None


class StudentUpdate(BaseModel):
    name: Optional[str] = None
    roll_no: Optional[str] = None
    email: Optional[str] = None
    department: Optional[str] = None
    year: Optional[int] = None
    phone: Optional[str] = None
    is_active: Optional[bool] = None


class StudentResponse(BaseModel):
    id: int
    name: str
    roll_no: str
    email: str
    department: Optional[str]
    year: Optional[int]
    phone: Optional[str]
    is_active: bool

    model_config = ConfigDict(from_attributes=True)


class DeleteResponse(BaseModel):
    message: str


# -------------------- AUTH SCHEMAS --------------------

class UserCreate(BaseModel):
    email: str
    password: str


class UserLogin(BaseModel):
    email: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str
