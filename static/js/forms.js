(function($) {

  $(document).ready(function () {

    $('input, textarea').on('keypress', function () {
      var $parent = $(this).parents('.has-error');
      $parent.removeClass('has-error');
      $parent.find('.help-block-error').remove();
    });

  });

})(jQuery);