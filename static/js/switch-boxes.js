(function ($) {

  $(document).ready(function () {

    $('[data-switch-target]').click(function (event) {
      event.preventDefault()

      var $this = $(this);

      if (typeof($this.attr('data-switch-active')) !== 'undefined') {
        return;
      }

      $('[data-switch-active]').removeAttr('data-switch-active');
      $this.attr('data-switch-active', true);

      $('[data-switch-item]').each(function (idx, el) {

        var $el = $(el);
        if ($el.attr('id') == $this.data('switch-target')) {
          $el.removeClass('card-inactive').addClass('card-active');
        } else {
          $el.removeClass('card-active').addClass('card-inactive');
        }

      });


    });

  });

})(jQuery);