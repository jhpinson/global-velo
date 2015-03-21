PIPELINE_ENABLED = True
PIPELINE_CSS_COMPRESSOR = None
PIPELINE_JS_COMPRESSOR = None
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_CSS = {
    'main': {
        'source_filenames': (
            'css/main.css',
            'css/dev.css',
            'css/dev-menu.css',
            'css/home-boxes.css',
            'css/forms.css',
        ),
        'output_filename': 'c/main.css',
    },

    'teasing': {
        'source_filenames': (
            'css/main.css',
            'css/dev.css',
            'css/forms.css',
            'css/teasing.css'
        ),
        'output_filename': 'c/teasing.css',
    },
}

PIPELINE_JS = {
    'lazy': {
        'source_filenames': (
            'js/ajax-form.js',
            'js/ajax-form-validation.js',
            'js/gmap.js',
            'js/switch-boxes.js',
            'js/forms.js',

        ),
        'output_filename': 'c/lazy.js',
    },
}
