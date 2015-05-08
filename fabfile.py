# encoding: utf-8
from __future__ import unicode_literals, absolute_import
from fabric.api import run, env, prefix, cd, require
from functools import wraps
import sys
from fabric.colors import red, green

from os import environ

def virtualenv(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        with prefix('source /usr/local/bin/virtualenvwrapper.sh'):
            with prefix('workon global-velo'):
                return func(*args, **kwargs)

    return decorated


def production():
    env.hosts = [
        environ.get('PROD_HOST', 'user@host')
    ]


def restart_uwsgi():
    run('sudo supervisorctl restart gv-uwsgi')


@virtualenv
def collectstatic():
    run('django-admin collectstatic --noinput')

def pull_current_branch():
    with cd("/home/jhpinson/virtualenvs/global-velo/global-velo"):
        run("git pull")

def flush_page_cache():
    run('redis-cli -n 2 flushdb')

def fullupdate():
    pull_current_branch()
    collectstatic()
    restart_uwsgi()
    flush_page_cache()

