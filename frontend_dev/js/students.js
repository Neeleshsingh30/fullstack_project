const API = "https://fullstack-project-10rd.onrender.com";

async function loadStudents() {
  const res = await fetch(`${API}/students`);
  const data = await res.json();

  const table = document.getElementById("studentsTable");
  table.innerHTML = "";

  data.forEach(s => {
    table.innerHTML += `
      <tr>
        <td>${s.name}</td>
        <td>${s.roll_no}</td>
        <td>${s.department}</td>
        <td>${s.year}</td>
        <td>
          <button onclick="editStudent(${s.id})">Edit</button>
          <button onclick="deleteStudent(${s.id})">Delete</button>
        </td>
      </tr>`;
  });
}

async function saveStudent() {
  const student = {
    name: name.value,
    roll_no: roll.value,
    email: email.value,
    department: dept.value,
    year: parseInt(year.value),
    phone: phone.value,
    is_active: true
  };

  await fetch(`${API}/students`, {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify(student)
  });

  alert("Student Added");
  location.href = "students.html";
}

async function deleteStudent(id) {
  await fetch(`${API}/students/${id}`, { method: "DELETE" });
  loadStudents();
}

function editStudent(id) {
  localStorage.setItem("editId", id);
  location.href = "add_edit_student.html";
}

if (document.getElementById("studentsTable")) {
  loadStudents();
}
