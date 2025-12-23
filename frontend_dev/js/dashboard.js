// =====================================
// Dashboard JS (Production Ready)
// =====================================

// 🔹 Backend API base URL (Render)
const API_BASE_URL = "https://fullstack-project-10rd.onrender.com";

// 🔹 Auth token
const token = localStorage.getItem("token");

// =====================================
// AUTH GUARD
// =====================================
(function authGuard() {
  if (!token) {
    // ❌ Token missing → redirect to login
    alert("Session expired. Please login again.");
    window.location.href = "login.html";
    return;
  }

  // ✅ Token present
  const statusEl = document.getElementById("status");
  if (statusEl) {
    statusEl.innerText = "✅ You are logged in successfully";
  }
})();

// =====================================
// NAVIGATION FUNCTIONS
// =====================================
function goStudents() {
  window.location.href = "students.html";
}

function goAddStudent() {
  window.location.href = "add_edit_student.html";
}

// =====================================
// LOGOUT
// =====================================
function logout() {
  localStorage.removeItem("token");
  alert("Logged out successfully");
  window.location.href = "login.html";
}

// =====================================
// DASHBOARD STATS (Future / Optional)
// =====================================
async function loadDashboardStats() {
  try {
    const response = await fetch(`${API_BASE_URL}/students`, {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
        "Authorization": `Bearer ${token}`
      }
    });

    // ❌ Token invalid / expired
    if (response.status === 401) {
      alert("Session expired. Please login again.");
      localStorage.removeItem("token");
      window.location.href = "login.html";
      return;
    }

    if (!response.ok) {
      throw new Error("Failed to fetch dashboard data");
    }

    const data = await response.json();
    console.log("Dashboard data loaded:", data);

    // 🔹 Example (future cards)
    // document.getElementById("totalStudents").innerText = data.length;

  } catch (error) {
    console.error("Failed to load dashboard stats:", error);
  }
}

// 🔹 Uncomment when dashboard cards are added
// loadDashboardStats();
