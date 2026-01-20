

function validateLoginForm() {
  const name = document.getElementById("name").value;
  const password = document.getElementById("password").value;
   

  if (name === "" || password === "") {
    alert("Please fill in all fields");
    return false;
  }
  if (password.length < 5) {
    alert("Password is too short");
    return false;
  }
  
  if (password.includes(" ")) {
    alert("Password is invalid");
    return false;
  }

  }
  
  document.getElementById('form').addEventListener("click",validateLoginForm)



//   function updateHeading(newHeading) {
//   const name= document.getElementById("name").value
//    let heading = document.querySelector("h3");
//    heading.innerHTML = newHeading;
//  }
 


