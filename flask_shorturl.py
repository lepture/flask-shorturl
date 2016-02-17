# coding: utf-8

from werkzeug.routing import BaseConverter, ValidationError

DEFAULT_ALPHABET = 'mn6j2c4rv8bpygw95z7hsdaetxuk3fq'
MIN_LENGTH = 5


__all__ = ['ShortUrl']


class UrlEncoder(object):
    """
    Author: Michael Fogleman
    License: MIT
    Link: http://code.activestate.com/recipes/576918/ (r3)
    """

    def __init__(self, alphabet, block_size=24):
        self.alphabet = alphabet
        self.block_size = block_size
        self.mask = (1 << block_size) - 1
        self.mapping = list(range(block_size))
        self.mapping.reverse()

    def encode_url(self, n, min_length=MIN_LENGTH):
        return self.enbase(self.encode(n), min_length)

    def decode_url(self, n):
        return self.decode(self.debase(n))

    def encode(self, n):
        return (n & ~self.mask) | self._encode(n & self.mask)

    def _encode(self, n):
        result = 0
        for i, b in enumerate(self.mapping):
            if n & (1 << i):
                result |= (1 << b)
        return result

    def decode(self, n):
        return (n & ~self.mask) | self._decode(n & self.mask)

    def _decode(self, n):
        result = 0
        for i, b in enumerate(self.mapping):
            if n & (1 << b):
                result |= (1 << i)
        return result

    def enbase(self, x, min_length=MIN_LENGTH):
        result = self._enbase(x)
        padding = self.alphabet[0] * (min_length - len(result))
        return '%s%s' % (padding, result)

    def _enbase(self, x):
        n = len(self.alphabet)
        if x < n:
            return self.alphabet[int(x)]
        return self._enbase(int(x / n)) + self.alphabet[int(x % n)]

    def debase(self, x):
        n = len(self.alphabet)
        result = 0
        for i, c in enumerate(reversed(x)):
            result += self.alphabet.index(c) * (n ** i)
        return result


def ShortUrlConverter_factory(su):  # noqa
    class ShortUrlConverter(BaseConverter):
        """
        ShortUrl converter for the Werkzeug routing system.
        """

        def __init__(self, map):
            super(ShortUrlConverter, self).__init__(map)
            self._su = su

        def to_python(self, value):
            try:
                return self._su.decode_url(value)
            except ValueError:
                raise ValidationError()

        def to_url(self, value):
            return self._su.encode_url(value)

    return ShortUrlConverter


class ShortUrl(object):
    """
    ShortUrl Interface.

    Create an instance is simple::

        su = ShortUrl(app)

    You can also pass the app of Flask later::

        su = ShortUrl()
        su.init_app(app)

    :param app: the app instance of Flask
    """

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)
        else:
            self.app = None

    def init_app(self, app):
        app.config.setdefault('SHORT_URL_ALPHABET', DEFAULT_ALPHABET)
        app.config.setdefault('SHORT_URL_MIN_LENGTH', MIN_LENGTH)
        app.config.setdefault('SHORT_URL_BLOCK_SIZE', 24)

        self.app = app
        app.extensions = getattr(app, 'extensions', {})
        app.extensions['short_url'] = self
        app.url_map.converters['short_url'] = ShortUrlConverter_factory(self)

    def get_app(self):
        if self.app is not None:
            return self.app

        from flask import _app_ctx_stack
        ctx = _app_ctx_stack.top
        if ctx is not None:
            return ctx.app
        raise RuntimeError(
            'application not registered on ShortUrl '
            'instance and no application bound to current context'
        )

    @property
    def encoder(self):
        if hasattr(self, '_encoder'):
            return self._encoder

        app = self.get_app()
        alphabet = app.config.get('SHORT_URL_ALPHABET')
        block_size = app.config.get('SHORT_URL_BLOCK_SIZE', 24)
        self._encoder = UrlEncoder(alphabet=alphabet, block_size=block_size)
        return self._encoder

    def encode(self, n):
        return self.encoder.encode(n)

    def decode(self, n):
        return self.encoder.decode(n)

    def enbase(self, n):
        app = self.get_app()
        min_length = app.config.get('SHORT_URL_MIN_LENGTH')
        return self.encoder.enbase(n, min_length)

    def debase(self, n):
        return self.encoder.debase(n)

    def encode_url(self, n):
        """
        Encode the id number to a short url.

        ::

            >>> su = ShortUrl()
            >>> su.encode_url(12)
        """
        app = self.get_app()
        min_length = app.config.get('SHORT_URL_MIN_LENGTH')
        return self.encoder.encode_url(n, min_length)

    def decode_url(self, n):
        """
        Decode the short url into the id number.

        ::

            >>> su = ShortUrl()
            >>> su.decode_url('zkf2n')
        """
        return self.encoder.decode_url(n)
