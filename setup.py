import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

VERSION = '0.1.0'

if sys.argv[-1] == 'publish':
    os.system('rm -rf *.egg-info')
    os.system('rm -rf build')
    os.system('rm -rf dist')
    os.system('git clean -x -f')
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name = 'dcdumper',
    author = 'A. Rothfusz',
    author_email = 'support@dotcloud.com',
    url = 'http://www.dotcloud.com/',
    version = VERSION,
    packages = [
    ],
    scripts  = [
        'dcdumper'
    ],
    install_requires = ['dotcloud==0.9.4'],
    zip_safe = False,
    description = 'hacked dotCloud command-line interface client',
    long_description =
    'An alternative to the dotCloud CLI, now with utilities to help with backups.'
)
