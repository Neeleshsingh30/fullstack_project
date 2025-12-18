from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class StudentResponse(BaseModel):
    id: int
    name: str
    roll_no: str
    email: str
    department: Optional[str]
    year: Optional[int]
    phone: Optional[str]
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True   # ✅ Pydantic v2 fix
