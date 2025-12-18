from sqlalchemy.orm import Session
from .models import Student
from schemas import StudentCreate, StudentUpdate

def create_student(db: Session, student: StudentCreate):
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student


def get_students(db: Session):
    return db.query(Student).all()


def get_student_by_id(db: Session, student_id: int):
    return db.query(Student).filter(Student.id == student_id).first()


def update_student(db: Session, student_id: int, student: StudentUpdate):
    db_student = get_student_by_id(db, student_id)
    if not db_student:
        return None

    for key, value in student.dict(exclude_unset=True).items():
        setattr(db_student, key, value)

    db.commit()
    db.refresh(db_student)
    return db_student


def delete_student(db: Session, student_id: int):
    student = get_student_by_id(db, student_id)
    if not student:
        return None
    student.is_active = False   # Soft delete
    db.commit()
    return student
