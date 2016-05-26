PIPELINE_ENABLED = True
PIPELINE_CSS_COMPRESSOR = None
PIPELINE_JS_COMPRESSOR = None
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_CSS = {
    'main': {
        'source_filenames': (
            'css/main.css',
        ),
        'output_filename': 'c/main.css',
    },

   
}

PIPELINE_JS = {
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
