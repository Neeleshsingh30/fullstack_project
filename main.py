from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import DeleteResponse
from database import SessionLocal
from models import Student
from schemas import StudentCreate, StudentUpdate, StudentResponse
import crud

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET
@app.get("/students", response_model=list[StudentResponse])
def get_students(db: Session = Depends(get_db)):
    return db.query(Student).all()

# POST
@app.post("/students", response_model=StudentResponse)
def add_student(student: StudentCreate, db: Session = Depends(get_db)):
    return crud.create_student(db, student)

# PUT
@app.put("/students/{student_id}", response_model=StudentResponse)
def update_student(
    student_id: int,
    student: StudentUpdate,
    db: Session = Depends(get_db)
):
    db_student = db.query(Student).filter(Student.id == student_id).first()

    if not db_student:
        raise HTTPException(status_code=404, detail="Student not found")

    for key, value in student.dict(exclude_unset=True).items():
        setattr(db_student, key, value)

    db.commit()
    db.refresh(db_student)
    return db_student

# delete method
@app.delete("/students/{student_id}", response_model=DeleteResponse)
def delete_student(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()

    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()

    return {"message": "Student deleted successfully"}
