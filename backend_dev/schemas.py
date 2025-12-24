# ================================
# IMPORTS
# ================================
from pydantic import BaseModel, ConfigDict
from typing import Optional


# =====================================================
# STUDENT SCHEMAS
# =====================================================

# -------------------------------
# StudentCreate
# Used in POST /students
# Input schema (request body)
# -------------------------------
class StudentCreate(BaseModel):
    name: str
    roll_no: str
    email: str
    department: Optional[str] = None
    year: Optional[int] = None
    phone: Optional[str] = None


# -------------------------------
# StudentUpdate
# Used in PUT /students/{id}
# All fields optional (partial update)
# -------------------------------
class StudentUpdate(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    year: Optional[int] = None
    phone: Optional[str] = None
    is_active: Optional[bool] = None


# -------------------------------
# StudentResponse
# Used as response_model
# Converts SQLAlchemy object → JSON
# -------------------------------
class StudentResponse(BaseModel):
    id: int
    name: str
    roll_no: str
    email: str
    department: Optional[str]
    year: Optional[int]
    phone: Optional[str]
    is_active: bool

    # Pydantic v2 config
    model_config = ConfigDict(from_attributes=True)


# -------------------------------
# DeleteResponse
# Used in DELETE /students/{id}
# -------------------------------
class DeleteResponse(BaseModel):
    message: str


# =====================================================
# USER / AUTHENTICATION SCHEMAS
# =====================================================

# -------------------------------
# UserCreate
# Used in POST /signup
# Takes plain password (will be hashed in backend)
# -------------------------------
class UserCreate(BaseModel):
    email: str
    password: str


# -------------------------------
# UserLogin
# Used in POST /login
# -------------------------------
class UserLogin(BaseModel):
    email: str
    password: str


# -------------------------------
# Token
# Used as response of /login
# JWT token returned to client
# -------------------------------
class Token(BaseModel):
    access_token: str
    token_type: str
