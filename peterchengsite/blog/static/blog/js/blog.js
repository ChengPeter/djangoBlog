$(document).ready(function(){
      /*$('ul.nav > li').click(function (e) {
      //e.preventDefault();
      $('ul.nav > li').removeClass("active");
      $(this).addClass("active");
      })*/
      $("#search").focus(function(){
          $("#myModal").modal("toggle");
      });
       $(document).scroll(function(){
      if($(document).scrollTop() > 400)
      {
        $("#back-to-top").fadeIn(100);
      }
      else{
        $("#back-to-top").fadeOut(100);
      }
      });
      $("#back-to-top").click(function(){
        $('html, body').animate({scrollTop: 0}, 200); 
      });
    });