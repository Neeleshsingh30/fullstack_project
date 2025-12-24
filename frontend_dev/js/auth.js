// ===============================
// AUTH.JS — ERROR-AWARE VERSION
// ===============================

const API_BASE_URL = "https://fullstack-project-10rd.onrender.com";

const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", async function (e) {
  e.preventDefault();

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();

  if (!email || !password) {
    alert("Please enter email and password");
    return;
  }

  try {
    const response = await fetch(`${API_BASE_URL}/login`, {
      method: "POST",
      mode: "cors",                    // ✅ IMPORTANT
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email, password }),
    });

    // ✅ Safely parse response
    let data = {};
    const contentType = response.headers.get("content-type");

    if (contentType && contentType.includes("application/json")) {
      data = await response.json();
    }

    if (!response.ok) {
      alert(data.detail || "Login failed ❌");
      return;
    }

    if (!data.access_token) {
      alert("Login failed: Token missing ❌");
      return;
    }

    // 🔐 Save JWT token (consistent key)
    localStorage.setItem("token", data.access_token);

    alert("Login successful ✅");
    window.location.href = "dashboard.html";

  } catch (error) {
    console.error("Login network error:", error);

    alert(
      "Cannot reach backend.\n" +
      "• Check backend URL\n" +
      "• Check CORS\n" +
      "• Try again after refresh"
    );
  }
});
