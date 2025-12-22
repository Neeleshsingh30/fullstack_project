const BASE_URL = "https://fullstack-project-cg4r.onrender.com";

fetch(`${BASE_URL}/students`)
  .then(res => res.json())
  .then(data => console.log(data));
