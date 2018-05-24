#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages
import grm

setup(
    name='git-remote-manager',
    version=grm.__version__,
    author='Floyda',
    author_email='floyda@163.com',
    license='MIT',
    description='Git Remote Manager',
    long_description='Git Remote Manager',
    keywords='git remote private server',
    url='https://github.com/FloydaGithub/git-remote-manager',
    packages=[
        'grm',
    ],
    package_data={},
    install_requires=[
        'click >= 6.7',
    ],
    scripts=['bin/grm'],
)
