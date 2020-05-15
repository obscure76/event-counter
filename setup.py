#!/usr/bin/env python

from distutils.core import setup
from setuptools import setup, find_packages

setup(name='Eventcounter',
      version='1.0',
      description='A Simple event counter',
      author='Midhun Chinta',
      author_email='midhun.nitw@gmail.com',
      url='https://github.com/obscure76/event-counter',
      packages=find_packages(where='eventcounter'),
      package_dir={'': 'eventcounter'},
      python_requires='>=3.5, <4',
     )
