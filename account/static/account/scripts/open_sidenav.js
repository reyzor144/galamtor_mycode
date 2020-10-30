function openNav() {
  let menu = document.getElementsByClassName("sidenavbar");
  menu[0].style.width = "250px";
  // document.getElementById("main").style.marginLeft = "250px";
}

function closeNav() {
  let menu = document.getElementsByClassName("sidenavbar");
  menu[0].style.width = "0";
  // document.getElementById("main").style.marginLeft = "0";
}