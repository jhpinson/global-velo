(function ($) {

    $.fn.extend({

        cleanFormErrors: function () {
            var $this = $(this);
            $this.find('.help-block-error').remove();
            $this.find('.control-group.has-error').removeClass('has-error');
            $this.find('.message.error').hide();
        },

        setFormErrors: function (errors) {
            var $this = $(this);
            if (errors.messages) {
                html = "";
                for (var i = 0, l = errors.messages.length; i < l; i++) {
                    html += '<p>'
                        + errors.messages[i]
                        + '</p>';
                }
                if (html != "") {
                    $this.find('.message.error').html(html);
                    $this.find('.message.error').show();

                }
            }
            // form fields errors
            for (k in errors.details) {
                var field = errors.details[k];
                var html;
                var $parent = $this.find('[name='+ k +']').closest('.control-group');
                if (typeof field === 'function') {
                    continue;
                }
                $parent.addClass('has-error');

                for (var i = 0, j = field.length; i < j; i++) {
                    html = '<span class="help-block help-block-error"><strong>' + field[i] + '</strong></span>'
                    $parent.append(html)
                }


            }
        }});

})(jQuery);