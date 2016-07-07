Flask-ShortUrl
==================================

.. image:: https://img.shields.io/badge/donate-lepture-green.svg
   :target: https://lepture.herokuapp.com/?amount=500&reason=lepture%2Fflask-shorturl
   :alt: Donate lepture
.. image:: https://img.shields.io/pypi/wheel/flask-shorturl.svg
   :target: https://pypi.python.org/pypi/flask-shorturl/
   :alt: Wheel Status
.. image:: https://img.shields.io/pypi/v/flask-shorturl.svg
   :target: https://pypi.python.org/pypi/flask-shorturl/
   :alt: Latest Version
.. image:: https://travis-ci.org/lepture/flask-shorturl.svg?branch=master
   :target: https://travis-ci.org/lepture/flask-shorturl
   :alt: Travis CI Status
.. image:: https://coveralls.io/repos/lepture/flask-shorturl/badge.svg?branch=master
   :target: https://coveralls.io/r/lepture/flask-shorturl
   :alt: Coverage Status


Short URL generator for Flask Project.


Installation
------------

To install Flask-Shorturl, simply::

    $ pip install Flask-ShortUrl

Or alternatively if you don't have pip::

    $ easy_install Flask-ShortUrl


Usage
-----

You can initialize the app::

    from flask_shorturl import ShortUrl

    su = ShortUrl(app)

    url = su.encode_url(12)
    uid = su.decode_url(url)

You may also init the app later::

    su = ShortUrl()
    su.init_app(app)


Configuration
--------------

Configurations for Flask project:


======================   =====================================================
`SHORT_URL_ALPHABET`     The alphabet to be used by Encoder,
                         default value: ``mn6j2c4rv8bpygw95z7hsdaetxuk3fq``
`SHORT_URL_MIN_LENGTH`   default value: 5
`SHORT_URL_BLOCK_SIZE`   default value: 24
======================   =====================================================


Thanks
------

UrlEncoder from by `Michael Fogleman`_.

.. _`Michael Fogleman`: http://code.activestate.com/recipes/576918/
