#!/usr/bin/env python
# coding: utf-8


from setuptools import setup

setup(
    name='Flask-ShortUrl',
    version='0.1.0',
    url='https://github.com/lepture/flask-shorturl',
    author='Hsiaoming Yang',
    author_email='me@lepture.com',
    description='Short URL generaotr for Flask',
    long_description=open('README.rst').read(),
    license=open('LICENSE').read(),
    py_modules=['flask_shorturl'],
    platforms='any',
    install_requires=['Flask'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
