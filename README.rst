Flask-ShortUrl
==================================

Short URL generator for Flask Project.


Installation
------------

To install terminal, simply::

    $ pip install Flask-ShortUrl


Usage
-----

::

    from flask_shorturl import ShortUrl

    su = ShortUrl(app)

    url = su.encode_url(12)
    uid = su.decode_url(url)


Config
------

* SHORT_URL_ALPHABET: 'mn6j2c4rv8bpygw95z7hsdaetxuk3fq'
* SHORT_URL_MIN_LENGTH: 5
* SHORT_URL_BLOCK_SIZE: 24


Thanks
------

UrlEncoder from by `Michael Fogleman`_.

.. _`Michael Fogleman`: http://code.activestate.com/recipes/576918/
