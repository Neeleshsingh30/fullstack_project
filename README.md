# Student Database Management System

A **full-stack Student Database Management System** developed using **FastAPI, PostgreSQL, and Vanilla JavaScript**, focused on **secure authentication, student record management, and a clean dashboard UI**.

This project is built **from scratch**, covering backend API development, database integration, authentication, and frontend dashboard implementation.

---

## Project Objective

The main goal of this project is to:

* Learn and implement **FastAPI with PostgreSQL**
* Build **JWT-based authentication**
* Perform **CRUD operations** on student data
* Design a **secure, protected dashboard**
* Follow **real-world project structure and practices**

This project is suitable for:

* Academic projects
* Backend / Full-Stack interviews
* Learning REST APIs with authentication

---

## Tech Stack Used

### 🔹 Backend

* **FastAPI**
* **SQLAlchemy ORM**
* **PostgreSQL**
* **JWT Authentication**
* **Pydantic Schemas**
* **Uvicorn**

### 🔹 Frontend

* **HTML**
* **CSS (custom glassmorphism UI)**
* **JavaScript (Fetch API)**
* **JWT stored in LocalStorage**

---

## Project Structure

```text
student-db-project/
│
├── backend/
│   ├── main.py            # FastAPI app (auth + student APIs)
│   ├── database.py        # PostgreSQL connection
│   ├── models.py          # SQLAlchemy models
│   ├── schemas.py         # Pydantic schemas
│   ├── crud.py            # Database operations
│   ├── auth.py            # Password hashing
│   ├── security.py        # JWT token logic
│
└── frontend_dev/
    ├── css/
    │   └── style.css
    │
    ├── js/
    │   └── students.js
    │
    ├── index.html          # Home page
    ├── login.html          # Login page
    ├── signup.html         # Signup page
    ├── dashboard.html      # Dashboard
    ├── students.html       # Students list (View / Delete)
    └── add_edit_student.html # Add & Edit student
```

---

## Authentication Flow (Implemented)

1. User registers using **Signup**
2. User logs in using **Login**
3. Backend verifies credentials and generates a **JWT access token**
4. Token is stored in **browser localStorage**
5. Token is sent in request headers for protected APIs
6. Unauthorized users are redirected to login page

```http
Authorization: Bearer <JWT_TOKEN>
```

---

## Features Implemented

### Authentication

* User signup
* User login
* Password hashing
* JWT token generation and validation

### Student Management

* View all students
* Add new student
* Edit existing student
* Delete student
* Active / Inactive status handling

### Dashboard

* Protected dashboard (JWT required)
* Sidebar navigation
* Students list in tabular format
* Add/Edit student using single form page
* Logout functionality

---

## API Endpoints

### Authentication APIs

| Method | Endpoint  | Description       |
| ------ | --------- | ----------------- |
| POST   | `/signup` | Register new user |
| POST   | `/login`  | Login and get JWT |

### Student APIs (JWT Protected)

| Method | Endpoint           | Description       |
| ------ | ------------------ | ----------------- |
| GET    | `/students`        | Get all students  |
| GET    | `/students/{id}`   | Get student by ID |
| POST   | `/students`        | Add student       |
| PUT    | `/students/{id}`   | Update student    |
| DELETE | `/students/{id}`   | Delete student    |
| GET    | `/students/filter` | Filter students   |

---

## Setup Instructions (From Scratch)

### Clone Repository

```bash
git clone https://github.com/NeeleshSingh/student-db-project.git
cd student-db-project
```

---

### Backend Setup

#### Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

#### Install dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary passlib[bcrypt] python-jose
```

#### Start backend server

```bash
uvicorn main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```

Fronted URL :

```
https://fullstack-project-frontend-rj28.onrender.com
```

---

### 3️⃣ PostgreSQL Configuration

* Create a PostgreSQL database
* Update credentials in `database.py`
* Tables are auto-created on server startup

---

### 4️⃣ Frontend Setup

* Open `frontend_dev` folder
* Run using Live Server OR open `index.html`
* Ensure backend server is running

---

## 🧪 How to Use the Application

1. Open `index.html`
2. Signup with email & password
3. Login
4. Access dashboard
5. View students
6. Add / Edit / Delete students
7. Logout

---

## 📌 What This Project Demonstrates

* REST API design using FastAPI
* JWT authentication implementation
* PostgreSQL integration with SQLAlchemy
* Frontend & backend separation
* Secure route handling
* Clean, modular project structure

---

## 🚀 Future Improvements

* Pagination & sorting
* Advanced filtering UI
* Dashboard analytics (charts)
* Role-based access (Admin/User)
* Light/Dark mode toggle

---

## 👨‍💻 Developer

**Neelesh Singh**
B.Tech – Computer Technology (AI Focus)
Python | FastAPI | PostgreSQL | Data Analytics | Machine Learning

---

## ⭐ Final Note

This project was developed as a **hands-on learning project**, focusing on **practical backend development, authentication, and CRUD workflows**.

If you find this project useful, consider giving it a ⭐ on GitHub.

---
