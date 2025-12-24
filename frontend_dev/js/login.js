// ===============================
// LOGIN.JS — FINAL FIXED VERSION
// ===============================

const API_BASE_URL = "https://fullstack-project-10rd.onrender.com";

// 🔐 If token already exists, redirect to dashboard
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
    // ✅ CONFIRMED LOGIN ENDPOINT
    const response = await fetch(`${API_BASE_URL}/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ email, password })
    });

    // ✅ SAFE JSON PARSING
    let data = {};
    try {
      data = await response.json();
    } catch {}

    if (!response.ok) {
      loginMsg.textContent =
        data.detail || data.message || "Invalid credentials";
      loginMsg.style.color = "red";
      return;
    }

    const token = data.access_token || data.token;
    if (!token) {
      loginMsg.textContent = "Token not received from server";
      loginMsg.style.color = "red";
      return;
    }

    localStorage.setItem("token", token);

    loginMsg.textContent = "Login successful ✔ Redirecting...";
    loginMsg.style.color = "green";

    setTimeout(() => {
      window.location.href = "dashboard.html";
    }, 800);

  } catch (error) {
    console.error("Login error:", error);
    loginMsg.textContent = "Server not responding ❌";
    loginMsg.style.color = "red";
  }
});
