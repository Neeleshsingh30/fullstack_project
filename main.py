from database import SessionLocal
from models import Student

# DB session create
db = SessionLocal()

# 🔹 All students fetch
students = db.query(Student).all()

for s in students:
    print(
        s.id,
        s.name,
        s.roll_no,
        s.email,
        s.department,
        s.year
    )

db.close()
