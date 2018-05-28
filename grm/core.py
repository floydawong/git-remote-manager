# -*- coding: utf-8 -*-
# Author: Floyda

from multiprocessing import Process
import os
from utils import Logging, run_command, get_public_ip, open_file
from macro import BASE_GRM_DIR, REPO_POSTFIX, CONFIG_FILE

# ------------------ Split Line By Floyda ------------------
# Methods
# ------------------ Split Line By Floyda ------------------

PUBILC_URL = None


def _get_pubilc_url(path):
    global PUBILC_URL
    if not PUBILC_URL:
        PUBILC_URL = get_config(path, 'public_ip')
    return PUBILC_URL


def wrap_repo_url(path, name):
    url = _get_pubilc_url(path)
    return "git@%s:%s/%s" % (url, os.path.abspath(path), name)


def wrap_repo_name(name):
    return name + REPO_POSTFIX


def check_repo_validity(name):
    return REPO_POSTFIX in name


def check_path(func):
    def wrapper(*args, **kwargs):
        path = args[0]
        grm_path = os.path.join(path, BASE_GRM_DIR)
        if not os.path.exists(grm_path):
            Logging.error(
                "fatal: not a remote root directory(%s)" % BASE_GRM_DIR)
            return
        return func(*args, **kwargs)

    return wrapper


# ------------------ Split Line By Floyda ------------------
# Config
# ------------------ Split Line By Floyda ------------------
import json


def init_config(path):
    fname = os.path.join(path, BASE_GRM_DIR, CONFIG_FILE)
    with open(fname, 'w') as fp:
        fp.write('{}')


def get_config(path, key, default=None):
    fname = os.path.join(path, BASE_GRM_DIR, CONFIG_FILE)
    with open(fname, 'r') as fp:
        try:
            config = json.load(fp)
        except:
            config = {}

    return config.get(key, default)


def set_config(path, key, value):
    fname = os.path.join(path, BASE_GRM_DIR, CONFIG_FILE)
    with open(fname, 'w') as fp:
        try:
            config = json.load(fp)
        except:
            config = {}

        config[key] = value
        content = json.dumps(
            config, sort_keys=True, indent=4, separators=(',', ': '))
        fp.write(content)


# ------------------ Split Line By Floyda ------------------
# API
# ------------------ Split Line By Floyda ------------------
def init_public_ip():
    set_config('.', 'public_ip', get_public_ip())
    Logging.info('Initialized config : [public_ip]')


def init_root_repos(path):
    grm_path = os.path.join(path, BASE_GRM_DIR)
    if os.path.exists(grm_path):
        Logging.error('Reinitialized existing remote root directory in %s' %
                      os.path.abspath(path))
        return False

    if not os.path.exists(path):
        os.mkdir(path)
    Logging.info(
        'Initialized remote root directory in %s' % os.path.abspath(path))
    os.chdir(path)
    os.mkdir(BASE_GRM_DIR)

    init_config('.')
    p = Process(target=init_public_ip)
    p.start()


@check_path
def add(path, name):
    ''' Create a repository. '''
    os.chdir(path)
    name = wrap_repo_name(name)
    repo_name = os.path.join(path, name)
    if os.path.exists(repo_name):
        Logging.error('the repository is existent')
        return False

    run_command('git init --bare %s' % name)
    run_command('chown -R git:git %s' % name)

    repo_url = wrap_repo_url(path, name)
    Logging.info("repository url: %s" % (repo_url))
    Logging.info("git clone:      git clone %s" % (repo_url))
    Logging.info("git remote:     git remote add origin %s" % (repo_url))


@check_path
def remove(path, name):
    ''' Remove a repository. '''
    os.chdir(path)
    run_command('rm -fr %s' % name)

    name = wrap_repo_name(name)
    run_command('rm -fr %s' % name)


@check_path
def list(path):
    ''' List existing repository. '''
    os.chdir(path)
    for name in os.listdir(path):
        if check_repo_validity(name):
            repo_url = wrap_repo_url(path, name)
            name = name.replace(REPO_POSTFIX, '')
            Logging.info('%s  %80s' % (name, repo_url))


@check_path
def migrate(path, url):
    ''' Migrate the repositorys to other remote. '''
    print('migrate')


@check_path
def config(path):
    ''' Edit the config.  '''
    fname = os.path.join(path, BASE_GRM_DIR, CONFIG_FILE)
    open_file(os.path.abspath(fname))


def version():
    ''' Show version and exit. '''
    from . import __version__
    Logging.info(__version__)


# ------------------ Split Line By Floyda ------------------
# Main
# ------------------ Split Line By Floyda ------------------
if __name__ == '__main__':
    pass
