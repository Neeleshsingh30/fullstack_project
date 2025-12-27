from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from typing import Optional
from database import SessionLocal, engine, Base
from models import Student, User
from schemas import (
    StudentCreate, StudentUpdate, StudentResponse,
    DeleteResponse, UserCreate, UserLogin, Token
)
import crud
from auth import hash_password, verify_password
from security import create_access_token, get_current_user

app = FastAPI(title="Student Management API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def root():
    return {"message": "Backend running successfully"}


# ---------------- AUTH ----------------

@app.post("/signup")
def signup(user: UserCreate, db: Session = Depends(get_db)):
    existing = db.query(User).filter(User.email == user.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_user = User(
        email=user.email,
        hashed_password=hash_password(user.password)
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User registered successfully"}


@app.post("/login", response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user or not verify_password(user.password, str(db_user.hashed_password)):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}


# ---------------- STUDENTS ----------------

@app.get("/students", response_model=List[StudentResponse])
def get_students(
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Student).all()


@app.post("/students", response_model=StudentResponse)
def add_student(
    student: StudentCreate,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return crud.create_student(db, student)


@app.get("/students/{student_id}", response_model=StudentResponse)
def get_student(
    student_id: int,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return crud.get_student_by_id(db, student_id)


@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student: StudentUpdate,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return crud.update_student(db, student_id, student)


@app.delete("/students/{student_id}", response_model=DeleteResponse)
def delete_student(
    student_id: int,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return crud.delete_student(db, student_id)


@app.get("/students/filter", response_model=List[StudentResponse])
def filter_students(
    name: Optional[str] = None,
    department: Optional[str] = None,
    year: Optional[int] = None,
    is_active: Optional[bool] = None,
    current_user: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return crud.filter_students(db, name, department, year, is_active)

