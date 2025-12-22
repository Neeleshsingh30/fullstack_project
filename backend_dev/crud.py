from sqlalchemy.orm import Session
from models import Student

def create_student(db: Session, student):
    new_student = Student(
        name=student.name,
        roll_no=student.roll_no,
        email=student.email,
        department=student.department,
        year=student.year,
        phone=student.phone
    )
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return new_student
