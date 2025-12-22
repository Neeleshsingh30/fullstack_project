import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# global variable to store created student id
created_student_id = None


# ----------------------------
# TEST 1: CREATE student (POST)
# ----------------------------
def test_create_student():
    global created_student_id

    payload = {
        "name": "Test User",
        "roll_no": "TEST101",
        "email": "testuser@gmail.com",
        "department": "AI",
        "year": 2,
        "phone": "9999999999"
    }

    response = client.post("/students", json=payload)

    assert response.status_code == 200
    data = response.json()

    created_student_id = data["id"]

    assert data["name"] == "Test User"
    assert data["email"] == "testuser@gmail.com"


# ----------------------------
# TEST 2: GET all students
# ----------------------------
def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


# ----------------------------
# TEST 3: UPDATE student (PUT)
# ----------------------------
def test_update_student():
    payload = {
        "department": "Machine Learning",
        "year": 3
    }

    response = client.put(f"/students/{created_student_id}", json=payload)

    assert response.status_code == 200
    data = response.json()

    assert data["department"] == "Machine Learning"
    assert data["year"] == 3


# ----------------------------
# TEST 4: DELETE student
# ----------------------------
def test_delete_student():
    response = client.delete(f"/students/{created_student_id}")

    assert response.status_code == 200
    assert response.json()["message"] == "Student deleted successfully"
