(function($){
  $(function(){

    $('.sidenav').sidenav();
    $('select').formSelect();

  }); 
})(jQuery); 

document.addEventListener('DOMContentLoaded', function() {
  var elems = document.querySelectorAll('.dropdown-trigger');
  var instances = M.Dropdown.init(elems);
  var elems = document.querySelectorAll('.modal');
  var instances = M.Modal.init(elems);
  var elems = document.querySelectorAll('.tooltipped');
  var instances = M.Tooltip.init(elems);
});

var close = document.getElementsByClassName("closebtn");
var i;

for (i = 0; i < close.length; i++) {
  close[i].onclick = function(){
    var div = this.parentElement;
    div.style.opacity = "0";
    setTimeout(function(){ div.style.display = "none"; }, 600);
  }
}

$(document).ready(function () {
  $(".sidenav").sidenav();

  var smallSidenav = false;
  $("#sidenav-toggle").click(function() {
      smallSidenav = !smallSidenav;
      $(this).find(".material-icons").text(smallSidenav ? 'chevron_right' : 'chevron_left');
      $("#left-sidenav").toggleClass("sidenav-small", smallSidenav);
  });
});