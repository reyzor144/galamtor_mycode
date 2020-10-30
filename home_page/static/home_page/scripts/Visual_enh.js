let my_dropdowns_btns = document.getElementsByClassName("course-dropdown-btn");

for (let i = 0; i < my_dropdowns_btns.length; ++i) {
  my_dropdowns_btns[i].addEventListener("click", function () {
    document.getElementById("myDropdown" + (i + 1).toString()).classList.toggle("show");
  });
}