#!/usr/bin/env python

from os.path import abspath, join, dirname
from platform import system
from shutil import copyfile

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='sync-back',
    version='0.1.0',
    description='RSync backup utility',
    long_description=open(abspath(join(dirname(__file__), 'README.md'))).read(),
    author='Mike Adamson',
    author_email='mikeatdot@gmail.com',
    url='https://github.com/mike-tr-adamson/sync-back',
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],

)
