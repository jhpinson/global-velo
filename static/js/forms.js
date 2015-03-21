(function($) {

  $(document).ready(function () {

    $('input, textarea').on('keypress', function () {
      $(this).parents('.has-error').removeClass('has-error');
    });

  });

})(jQuery);