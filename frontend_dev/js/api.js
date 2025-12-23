const BASE_URL = "https://fullstack-project-10rd.onrender.com";

fetch(`${BASE_URL}/students`)
  .then(res => res.json())
  .then(data => console.log(data));
