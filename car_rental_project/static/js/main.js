const date = new Date();
document.querySelector(".year").innerHTML = date.getFullYear();

document.addEventListener("DOMContentLoaded", () => {
  (document.querySelectorAll(".notification .delete") || []).forEach(($delete) => {
    var $notification = $delete.parentNode;

    $delete.addEventListener("click", () => {
      $notification.parentNode.removeChild($notification);
    });
  });
});

setTimeout(function () {
  $("#message").fadeOut("slow");
}, 5000);
