(function ($) {

  $(document).ready(function () {
    $('.nav-toggle').click(function (event) {
      event.preventDefault();
      $('#mnu-mobile').toggleClass('active');
    })
  });

})(jQuery);