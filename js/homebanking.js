//modo oscuro
let checkbox = document.getElementById("flexSwitchCheckDefault");

checkbox.addEventListener("change", function() {
    if (checkbox.checked) {
      darkmode();
    } else {
      nodark();
    }
  });

function darkmode() {
     document.body.classList.add('darkmode');
     checkbox.checked = true;
}

function nodark() {
  document.body.classList.remove("darkmode"); 
  checkbox.checked = false;
  }
