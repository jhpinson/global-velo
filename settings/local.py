
from cache import *
from common import *
from pipeline import *

DEBUG = True
THUMBNAIL_DEBUG = False
DISABLE_ROBOTS=True

PIPELINE_ENABLED = False
PIPELINE_STYLUS_BINARY = "/usr/local/bin/stylus"
INTERNAL_IPS = ('127.0.0.1')

INSTALLED_APPS += (
    'devserver',
)

DEVSERVER_MODULES = (
    #'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

)
DEVSERVER_TRUNCATE_SQL = False
