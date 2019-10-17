#!/usr/bin/env python

from os.path import abspath, dirname, join

try:
    from setuptools import setup
except ImportError as error:
    from distutils.core import setup

version_file = join(dirname(abspath(__file__)), 'src', 'RequestsLibrary', 'version.py')

with open(version_file) as file:
      code = compile(file.read(), version_file, 'exec')
      exec(code)

DESCRIPTION = """
Robot Framework keyword library wrapper around the HTTP client library requests, support protobuf.
"""[1:-1]


CLASSIFIERS = """
Development Status :: 5 - Production/Stable
License :: OSI Approved :: MIT License
Operating System :: OS Independent
Programming Language :: Python
Topic :: Software Development :: Testing
"""[1:-1]

setup(name         = 'protobuf-robotframework-requests',
      version      = VERSION,
      description  = 'This library is a frok from https://pypi.org/project/robotframework-requests/. Robot Framework keyword library wrapper around requests, support protobuf',
      long_description = DESCRIPTION,
      author       = 'Bulkan Savun Evcimen, Mikayel Mikirtumov',
      author_email = 'bulkan@gmail.com, mmikirtumov@gmail.com',
      url          = 'https://github.com/mmikirtumov/protobuf-robotframework-requests',
      license      = 'MIT',
      keywords     = 'robotframework testing test automation http client requests, support protobuf',
      platforms    = 'any',
      classifiers  = CLASSIFIERS.splitlines(),
      package_dir  = {'' : 'src'},
      packages     = ['RequestsLibrary'],
      package_data = {'RequestsLibrary': ['tests/*.txt']},
      install_requires=[
          'robotframework',
          'requests',
          'protobuf'
      ],
)

""" From now on use this approach

python setup.py sdist upload
git tag -a 1.2.3 -m 'version 1.2.3'
git push --tags"""
