# -*- coding: utf-8 -*-
# Author: Floyda

import core


def init(path):
    ''' Create a git remote root directory or reinitialize an existing one. '''
    core.init_root_repos(path)


def add(path, name):
    ''' Create a repository. '''
    core.add(path, name)


def remove(path, name):
    ''' Remove a repository. '''
    core.remove(path, name)


def list(path):
    ''' List existing repository. '''
    core.list(path)


def migrate(path, url):
    ''' Migrate the repositorys to other remote. '''
    core.migrate(path, url)


def config(path):
    ''' Edit the config.  '''
    core.config(path)


def version():
    ''' Show version and exit. '''
    core.version()
