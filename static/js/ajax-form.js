(function ($) {

    $(document).ready(function () {

        $('body').on('click', '[data-role=submit-button]', function (event) {
          event.preventDefault();
          $(this).parents('form[data-ajax-uri]').submit();
        });

        $('body').on('submit', 'form[data-ajax-uri]', function (event) {

            event.preventDefault();

            var $form = $(this);
            $form.cleanFormErrors();
            $form.find('.form-success').hide();
            var data = $form.serialize(true);

            $form.find('[data-role=submit-button]').attr('disabled', 'disabled');
            $('#form-success').hide();
            $.ajax({
                type: 'POST',
                url: $form.data('ajax-uri'),
                data: data,
                success: function (response) {
                    if (response.success === true) {

                        if (response.reset === true) {
                          $('form')[0].reset();
                        }


                        if (typeof(response['redirect-url']) !== 'undefined') {
                            var target = response['target'] ;
                            if (typeof(target) !== 'undefined' && target !== null && target !== '' ) {
                              $(target).load(response['redirect-url']);
                            } else {
                              document.location.href = response['redirect-url'];
                            }

                        } else {
                            $form.find('[data-show-on-success]').show();
                            $form.find('[data-hide-on-success]').hide();
                            $form.find('[data-role=submit-button]').removeAttr('disabled');
                        }
                    } else {
                        $form.setFormErrors(response.errors);
                        $form.find('[data-role=submit-button]').removeAttr('disabled');
                    }
                },
                error: function () {
                    $form.setFormErrors({'messages' : ['Une erreur s\'est produite.']});
                    $form.find('[data-role=submit-button]').removeAttr('disabled');
                }
            });
        });
    });

})(jQuery);