const API_BASE_URL = "https://fullstack-project-10rd.onrender.com";

document.getElementById("loginForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  const email = document.getElementById("email").value.trim();
  const password = document.getElementById("password").value.trim();

  // basic validation
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
      body: JSON.stringify({
        email: email,
        password: password,
      }),
    });

    const data = await response.json();

    if (response.ok) {
      // 🔐 SAVE JWT TOKEN
      localStorage.setItem("access_token", data.access_token);

      alert("Login successful ✅");
      console.log("JWT Token:", data.access_token);

      // redirect to dashboard / home
      window.location.href = "index.html";
    } else {
      alert(data.detail || "Invalid credentials ❌");
    }
  } catch (error) {
    console.error("Login error:", error);
    alert("Backend server not responding ❌");
  }
});
