$(document).ready(function () {
  $("#sidebarCollapse").on("click", function () {
    $("#sidebar, #content").toggleClass("active");
    $(".collapse.in").toggleClass("in");
    $("a[aria-expanded=true]").attr("aria-expanded", "false");
    document.getElementById("bodyContent").style.width = "100%";
  });
});

const menu = document.getElementById("menu-toggle");
const pastel = document.getElementById("iconito");
const barra = document.getElementById("wrapper");

menu.addEventListener("click", function () {
  if (pastel.classList.contains("fa-lock")) {
    barra.classList.remove("toggled");
    pastel.classList.remove("fa-lock");
    pastel.classList.add("fa-lock-open");
  } else {
    barra.classList.add("toggled");
    pastel.classList.remove("fa-lock-open");
    pastel.classList.add("fa-lock");
  }
});

(function () {
  "use strict";
  window.addEventListener(
    "load",
    function () {
      var forms = document.getElementsByClassName("needs-validation");

      var validation = Array.prototype.filter.call(forms, function (form) {
        form.addEventListener(
          "submit",
          function (event) {
            if (form.checkValidity() === false) {
              event.preventDefault();
              event.stopPropagation();
            }
            form.classList.add("was-validated");
          },
          false
        );
      });
    },
    false
  );
})();

/*
document.getElementById('play-button').addEventListener('click', function(){
  var icon = document.getElementById('icon');
  icon.classList.toggle('fa-pause');
  icon.classList.toggle('fa-play');
})*/
$(document).ready(function () {
  $("#dtDynamicVerticalScrollExample").DataTable({
    scrollY: "50vh",
    scrollCollapse: true,
  });
  $(".dataTables_length").addClass("bs-select");
});
