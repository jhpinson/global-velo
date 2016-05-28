# encoding: utf-8
from __future__ import unicode_literals, absolute_import

STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE = {
    'PIPELINE_ENABLED': False,
    'JS_COMPRESSOR': None,
    'CSS_COMPRESSOR': None,
    'STYLESHEETS': {

        'main': {
            'source_filenames': (
                'css/main.css',
            ),
            'output_filename': 'c/main.css',
        },
    },
    'JAVASCRIPT': {
        'lazy': {
            'source_filenames': (
                'js/ajax-form.js',
                'js/ajax-form-validation.js',
                'js/forms.js',
                'js/utils.js',
                'js/menu.js',

            ),
            'output_filename': 'c/lazy.js',
        },
    }
}
