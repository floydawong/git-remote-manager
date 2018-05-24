# -*- coding: utf-8 -*-
# Author: Floyda

# ------------------ Split Line By Floyda ------------------
# Config
# ------------------ Split Line By Floyda ------------------
import os
import json
from macro import BASE_GRM_DIR, CONFIG_FILE


class Config:
    _config = None

    @staticmethod
    def _load(path):
        if not Config._config:
            fname = os.path.join(path, BASE_GRM_DIR, CONFIG_FILE)
            with open(fname, 'r') as fp:
                try:
                    Config._config = json.load(fp)
                except:
                    Config._config = {}
        return Config._config

    @staticmethod
    def _save(path):
        fname = os.path.join(path, BASE_GRM_DIR, CONFIG_FILE)
        with open(fname, 'w') as fp:
            content = json.dumps(
                Config._config,
                sort_keys=True,
                indent=4,
                separators=(',', ': '))
            fp.write(content)

    @staticmethod
    def get(path, key):
        cfg = Config._load(path)
        return cfg.get(key)

    @staticmethod
    def set(path, key, value):
        cfg = Config._load(path)
        cfg[key] = value
        Config._save(path)


# ------------------ Split Line By Floyda ------------------
# Logging
# ------------------ Split Line By Floyda ------------------
import sys


class Logging:
    # TODO maybe the right way to do this is to use something like colorama?
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    MAGENTA = '\033[35m'
    RESET = '\033[0m'

    @staticmethod
    def _print(s, color=None):
        if color and sys.stdout.isatty() and sys.platform != 'win32':
            print(color + s + Logging.RESET)
        else:
            print(s)

    @staticmethod
    def debug(s):
        Logging._print(s, Logging.MAGENTA)

    @staticmethod
    def info(s):
        Logging._print(s, Logging.GREEN)

    @staticmethod
    def warning(s):
        Logging._print(s, Logging.YELLOW)

    @staticmethod
    def error(s):
        Logging._print(s, Logging.RED)


def run_command(cmd):
    os.system(cmd)


# ------------------ Split Line By Floyda ------------------
# get IP
# ------------------ Split Line By Floyda ------------------
from urllib2 import urlopen
from json import load


def get_public_ip():
    #ip = urlopen('http://ip.42.pl/raw').read()
    #ip = load(urlopen('http://jsonip.com'))['ip']
    ip = load(urlopen('http://httpbin.org/ip'))['origin']
    #ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
    return ip


def get_internal_ip():
    import socket
    host_name = socket.getfqdn(socket.gethostname())
    addr = socket.gethostbyname(host_name)
    return addr


# ------------------ Split Line By Floyda ------------------
# Timer
# ------------------ Split Line By Floyda ------------------
import time


class timer():
    def __init__(self, func, *args, **kwargs):
        self._func = func
        self._args = args
        self._kwargs = kwargs

    def __call__(self):
        timestamp = time.time()
        self._func(*self._args, **self._kwargs)
        print(time.time() - timestamp)


# ------------------ Split Line By Floyda ------------------
# Open file in different platform
# ------------------ Split Line By Floyda ------------------
import sys


def open_file(path):
    p = sys.platform

    command = '%s %s'
    func = ''

    if p == 'win32':
        func = 'start'
    elif p == 'darwin':
        func = 'open'
    else:
        func = 'vi'

    os.system(command % (func, path))
