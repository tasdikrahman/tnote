from __future__ import print_function
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import io
import codecs
import os
import sys

import tnote.tnote as tnote

here = os.path.abspath(os.path.dirname(__file__))

def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)

long_description = read('README.md')

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errcode = pytest.main(self.test_args)
        sys.exit(errcode)

setup(
    name='tnote',
    version=tnote.__version__,
    url='https://github.com/prodicus/tnote',
    license='MIT',
    author='prodicus',
    tests_require=['pytest'],
    install_requires=['args>=0.1.0',
                    'clint>=0.5.1',
                    'peewee>=2.8.0',
                    ],
    cmdclass={'test': PyTest},
    author_email='prodicus@outlook.com',
    description='A command line note taking app',
    long_description=long_description,
    packages=['tnote'],
    include_package_data=True,
    platforms='any',
    test_suite='tnote.test.test_tnote',
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Environment :: Desktop',
        'Intended Audience :: Developers'
        ],
    extras_require={
        'testing': ['pytest'],
    }
)