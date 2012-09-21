#!/usr/bin/env python
from distutils.core import setup

for cmd in ('egg_info', 'develop'):
    import sys
    if cmd in sys.argv:
        from setuptools import setup

version='0.2.1'

setup(
    name='fabric-taskset',
    version=version,
    author='Mikhail Korobov',
    author_email='kmike84@gmail.com',

    packages=['taskset'],
    url='https://github.com/kmike/fabric-taskset/',
    license = 'MIT license',
    description = """ Expose class members as Fabric tasks """,

    long_description = open('README.rst').read() + open('CHANGES.rst').read(),
    requires = ['Fabric (>= 1.1)'],

    classifiers=(
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ),
)
