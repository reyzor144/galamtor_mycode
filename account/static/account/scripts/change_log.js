let site_logo = document.getElementsByClassName("site-name");

site_logo[0].addEventListener("click", function () {
    // redirect("home");
    window.location.href = "http://127.0.0.1:8000/";
});