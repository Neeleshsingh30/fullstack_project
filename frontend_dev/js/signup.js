// ===============================
// SIGNUP.JS — FINAL CORRECT VERSION
// ===============================

const API_BASE_URL = "https://fullstack-project-10rd.onrender.com";

document.addEventListener("DOMContentLoaded", () => {
  const signupForm = document.getElementById("signupForm");

  if (!signupForm) {
    console.error("❌ Signup form not found");
    return;
  }

  signupForm.addEventListener("submit", async (e) => {
    e.preventDefault();

    const email = document.getElementById("email").value.trim();
    const password = document.getElementById("password").value.trim();
    const confirmPassword =
      document.getElementById("confirmPassword")?.value.trim();

    // -------------------------------
    // VALIDATIONS
    // -------------------------------
    if (!email || !password) {
      alert("Email and password are required");
      return;
    }

    if (confirmPassword !== undefined && password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }

    try {
      // ✅ FIXED: correct backend endpoint
      const response = await fetch(`${API_BASE_URL}/signup`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ email, password })
      });

      // ✅ Safe JSON parsing
      let data = {};
      try {
        data = await response.json();
      } catch {}

      if (!response.ok) {
        alert(data.detail || "❌ Signup failed");
        return;
      }

      alert("✅ Signup successful! Please login.");
      window.location.href = "login.html";

    } catch (error) {
      console.error("❌ Signup error:", error);
      alert("❌ Backend server not reachable");
    }
  });
});
