import sys
import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from typing import List, Optional

# -------------------------------
# Path fix (important for imports)
# -------------------------------
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# -------------------------------
# Project imports
# -------------------------------
from database import engine, Base, SessionLocal
from models import Student, User
from schemas import (
    StudentCreate,
    StudentUpdate,
    StudentResponse,
    DeleteResponse,
    UserCreate,
    UserLogin,
    Token
)
import crud
from auth import hash_password, verify_password
from security import create_access_token, get_current_user
from fastapi.middleware.cors import CORSMiddleware

# -------------------------------
# App init
# -------------------------------
app = FastAPI(title="Student Management API with JWT Auth")

# -------------------------------
# CORS
# -------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # frontend URL yahan allow hota hai
    allow_credentials=True,
    allow_methods=["*"],      # GET, POST, PUT, DELETE
    allow_headers=["*"],
)

# -------------------------------
# Create tables on startup
# -------------------------------
@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)

# -------------------------------
# DB Dependency
# -------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# -------------------------------
# Root route
# -------------------------------
@app.get("/")
def root():
    return {"message": "Backend running successfully"}
# =====================================================
# AUTHENTICATION ROUTES
# =====================================================

# -------------------------------
# SIGNUP
# -------------------------------
@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    try:
        existing_user = db.query(User).filter(User.email == user.email).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        hashed_pwd = hash_password(user.password)

        new_user = User(
            email=user.email,
            hashed_password=hashed_pwd
        )

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return {"message": "User registered successfully"}

    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Email already exists")

    except Exception as e:
        db.rollback()
        print("SIGNUP ERROR:", e)
        raise HTTPException(status_code=500, detail="Internal server error")

# -------------------------------
# LOGIN
# -------------------------------
@app.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    if not verify_password(user.password, str(db_user.hashed_password)):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": db_user.email}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }

# =====================================================
# STUDENT ROUTES (JWT PROTECTED)
# =====================================================

# -------------------------------
# GET ALL STUDENTS
# -------------------------------
@app.get("/students", response_model=List[StudentResponse])
def get_students(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Student).all()

# -------------------------------
# GET SINGLE STUDENT (ADD-ON ✅)
# -------------------------------
@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student_by_id(
    student_id: int,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student

# -------------------------------
# FILTER STUDENTS (ADD-ON ✅)
# -------------------------------
@app.get("/students/filter", response_model=List[StudentResponse])
def filter_students(
    department: Optional[str] = None,
    year: Optional[int] = None,
    is_active: Optional[bool] = None,
    search: Optional[str] = None,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    query = db.query(Student)

    if department:
        query = query.filter(Student.department == department)

    if year:
        query = query.filter(Student.year == year)

    if is_active is not None:
        query = query.filter(Student.is_active == is_active)

    if search:
        query = query.filter(Student.name.ilike(f"%{search}%"))

    return query.all()

# -------------------------------
# CREATE STUDENT
# -------------------------------
@app.post("/students", response_model=StudentResponse)
def add_student(
    student: StudentCreate,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return crud.create_student(db, student)

# -------------------------------
# UPDATE STUDENT
# -------------------------------
@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student: StudentUpdate,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    db_student = db.query(Student).filter(Student.id == student_id).first()

    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")

    for key, value in student.model_dump(exclude_unset=True).items():
        setattr(db_student, key, value)

    db.commit()
    db.refresh(db_student)
    return db_student

# -------------------------------
# DELETE STUDENT
# -------------------------------
@app.delete("/students/{student_id}", response_model=DeleteResponse)
def delete_student(
    student_id: int,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return {"message": "Student deleted successfully"}
