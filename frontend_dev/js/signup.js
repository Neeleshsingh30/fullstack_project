// ===============================
// SIGNUP.JS – Backend Connected (UPDATED)
// ===============================

// ✅ IMPORTANT: No extra space in URL
const API_BASE_URL = "https://fullstack-project-10rd.onrender.com";

// DOM ready
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
    const confirmPassword = document.getElementById("confirmPassword")?.value.trim();

    // -------------------------------
    // BASIC VALIDATIONS
    // -------------------------------
    if (!email || !password) {
      alert("Email and password are required");
      return;
    }

    if (confirmPassword !== undefined && password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }

    // -------------------------------
    // API CALL
    // -------------------------------
    try {
      const response = await fetch(`${API_BASE_URL}/signup`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          email,
          password
        })
      });

      const data = await response.json();

      // -------------------------------
      // RESPONSE HANDLING
      // -------------------------------
      if (response.ok) {
        alert("✅ Signup successful! Please login.");
        window.location.href = "login.html";
      } else {
        alert(data.detail || "❌ Signup failed");
      }

    } catch (error) {
      console.error("❌ Signup error:", error);
      alert("❌ Backend server not reachable");
    }
  });
});
