#!/usr/bin/env python
# coding: utf8
from distutils.core import setup

VERSION = '0.1'

setup(name='pybacktest',
      version=VERSION,
      description='pybacktest',
      author='Matvey Ezhov',
      url='https://github.com/ematvey/pybacktest',
      packages=['pybacktest'],
      install_requires=['numpy', 'pandas>=0.11', 'pyyaml']
      )
