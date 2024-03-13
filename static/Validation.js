
function validateLoginForm() {
  const name = document.getElementById("name").value;
  const password = document.getElementById("password").value;

  if (name === "" || password === "") {
    alert("Please fill in all fields");
    return false;
  }
 
  }
  if (password.length < 5) {
    alert("Password is too short");
    return false;
  }
  
  if (password.includes(" ")) {
    alert("Password is invalid");
    return false;
  }
  return true;

function validateRegisterForm() {
  const email = document.getElementById("name").value;
  const name = document.getElementById("email").value;
  const address = document.getElementById("Address").value;
  const password = document.getElementById("password").value;
  const confirm_password = document.getElementById("confirm password").value;

  if (
    name === "" ||
    address === "" ||
    contact === "" ||
    email === "" ||
    password === "" ||
    confirm_password === ""
  ) {
    alert("Please fill in all fields");
    console.log(email, password);
    return false;
  }

  if (password !== confirm_password) {
    alert("Passwords do not match");
    return false;
  }

  return true;
}