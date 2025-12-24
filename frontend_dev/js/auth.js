// ===============================
// AUTH.JS — FINAL & SAFE VERSION
// ===============================

const API_BASE_URL = "https://fullstack-project-10rd.onrender.com";

const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", async function (e) {
  e.preventDefault();

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();

  // Basic validation
  if (!email || !password) {
    alert("Please enter email and password");
    return;
  }

  try {
    const response = await fetch(`${API_BASE_URL}/login`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    // ✅ Safe JSON parsing
    let data = {};
    try {
      data = await response.json();
    } catch {
      data = {};
    }

    if (!response.ok) {
      alert(data.detail || "Invalid credentials ❌");
      return;
    }

    // ✅ FIX 1: Use consistent token key
    const token = data.access_token;

    if (!token) {
      alert("Token not received from server ❌");
      return;
    }

    // 🔐 SAVE JWT TOKEN
    localStorage.setItem("token", token);

    alert("Login successful ✅");

    // ✅ FIX 2: Correct redirect
    window.location.href = "dashboard.html";

  } catch (error) {
    console.error("Login error:", error);
    alert("Backend server not responding ❌");
  }
});
