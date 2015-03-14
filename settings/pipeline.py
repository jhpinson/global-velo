PIPELINE_ENABLED = True
PIPELINE_CSS_COMPRESSOR = None
PIPELINE_JS_COMPRESSOR = None
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_CSS = {
    'base': {
        'source_filenames': (
            'css/style.css',
        ),
        'output_filename': 'c/base.css',
    },
}
PIPELINE_COMPILERS = (
    'pipeline.compilers.stylus.StylusCompiler',
)