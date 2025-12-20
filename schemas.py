from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI, Depends, HTTPException


# POST / PUT ke liye (input)
class StudentCreate(BaseModel):
    name: str
    roll_no: str
    email: str
    department: Optional[str] = None
    year: Optional[int] = None
    phone: Optional[str] = None

class StudentUpdate(BaseModel):
    name: Optional[str] = None
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

    class Config:
        orm_mode = True

# DELETE response model
class DeleteResponse(BaseModel):
    message: str