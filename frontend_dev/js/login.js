// ===============================
// LOGIN.JS — CLEAN VERSION
// ===============================

const API_BASE_URL = "https://fullstack-project-10rd.onrender.com";

// 🔐 Agar pehle se token hai → direct dashboard
const existingToken = localStorage.getItem("token");
if (existingToken) {
  window.location.href = "dashboard.html";
}

// DOM elements
const loginForm = document.getElementById("loginForm");
const loginMsg = document.getElementById("loginMsg");

loginForm.addEventListener("submit", async function (e) {
  e.preventDefault();
  loginMsg.textContent = "Logging in...";
  loginMsg.style.color = "black";

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();

  if (!email || !password) {
    loginMsg.textContent = "Please fill all fields";
    loginMsg.style.color = "red";
    return;
  }

  try {
    const response = await fetch(`${API_BASE_URL}/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        email: email,
        password: password
      })
    });

    const data = await response.json();

    if (!response.ok) {
      loginMsg.textContent = data.detail || "Invalid credentials";
      loginMsg.style.color = "red";
      return;
    }

    // ✅ TOKEN SAVE
    localStorage.setItem("token", data.access_token);

    loginMsg.textContent = "Login successful ✔ Redirecting...";
    loginMsg.style.color = "green";

    // ✅ REDIRECT TO DASHBOARD
    setTimeout(() => {
      window.location.href = "dashboard.html";
    }, 800);

  } catch (error) {
    console.error("Login error:", error);
    loginMsg.textContent = "Server not responding ❌";
    loginMsg.style.color = "red";
  }
});
