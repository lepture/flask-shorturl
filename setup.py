#!/usr/bin/env python
# coding: utf-8

from setuptools import setup

setup(
    name='Flask-ShortUrl',
    version='0.2.0',
    url='https://github.com/lepture/flask-shorturl',
    author='Hsiaoming Yang',
    author_email='me@lepture.com',
    description='Short URL generaotr for Flask',
    long_description=open('README.rst').read(),
    license=open('LICENSE').read(),
    py_modules=['flask_shorturl'],
    zip_safe=False,
    platforms='any',
    install_requires=['Flask'],
    tests_require=['nose'],
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
