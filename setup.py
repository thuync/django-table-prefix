# -*- coding: utf-8 -*-
import os.path
from setuptools import setup


def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()


setup(
    name='django-table-prefix',
    version='1.0.1',
    keywords='django database',
    author='Thuy Nguyen <thuycn@cohost.club>',
    packages=['django_table_prefix'],
    url='https://github.com/thuync/django-table-prefix',
    license='BSD licence, see LICENCE',
    description='Allow specification of a global or per-app database table name prefix.',
    long_description=read('README.md'),
    requires=[
        'Django',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
    ]
)
