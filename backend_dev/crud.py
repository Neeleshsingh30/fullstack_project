from typing import Optional
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from models import Student


def create_student(db: Session, student):
    try:
        db_student = Student(
            name=student.name,
            roll_no=student.roll_no,
            email=student.email,
            department=student.department,
            year=student.year,
            phone=student.phone,
            is_active=True
        )
        db.add(db_student)
        db.commit()
        db.refresh(db_student)
        return db_student

    except IntegrityError as e:
        db.rollback()
        error_msg = str(e.orig)

        if "roll_no" in error_msg:
            msg = "Roll number already exists"
        elif "email" in error_msg:
            msg = "Email already exists"
        else:
            msg = "Database constraint violation"

        raise HTTPException(status_code=400, detail=msg)


def get_student_by_id(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return student


def update_student(db: Session, student_id: int, student_data):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    for key, value in student_data.dict(exclude_unset=True).items():
        setattr(student, key, value)

    try:
        db.commit()
        db.refresh(student)
        return student
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail="Roll number or email already exists"
        )


def delete_student(db: Session, student_id: int):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    db.delete(student)
    db.commit()
    return {"message": "Student deleted successfully"}


def filter_students(
    db: Session,
    name: Optional[str] = None,
    department: Optional[str] = None,
    year: Optional[int] = None,
    is_active: Optional[bool] = None
):

    query = db.query(Student)

    if name:
        query = query.filter(Student.name.ilike(f"%{name}%"))
    if department:
        query = query.filter(Student.department == department)
    if year is not None:
        query = query.filter(Student.year == year)
    if is_active is not None:
        query = query.filter(Student.is_active == is_active)

    return query.all()
