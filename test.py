from nose.tools import raises
from flask import Flask
from flask_shorturl import ShortUrl


def test_shorturl():
    app = Flask(__name__)

    su = ShortUrl(app)
    for a in range(0, 200000, 37):
        b = su.encode(a)
        c = su.enbase(b)
        d = su.debase(c)
        e = su.decode(d)
        assert a == e
        assert b == d
        assert c == su.encode_url(a)
        assert a == su.decode_url(c)


def test_init_app():
    app = Flask(__name__)
    su = ShortUrl()
    su.init_app(app)

    a = 21
    b = su.encode(a)
    c = su.enbase(b)
    d = su.debase(c)
    e = su.decode(d)
    assert a == e
    assert b == d
    assert c == su.encode_url(a)
    assert a == su.decode_url(c)


def test_flask_ctx():
    app = Flask(__name__)
    DEFAULT_ALPHABET = 'mn6j2c4rv8bpygw95z7hsdaetxuk3fq'
    app.config.setdefault('SHORT_URL_ALPHABET', DEFAULT_ALPHABET)
    app.config.setdefault('SHORT_URL_MIN_LENGTH', 5)
    app.config.setdefault('SHORT_URL_BLOCK_SIZE', 24)

    su = ShortUrl()

    with app.test_request_context():
        a = 21
        b = su.encode(a)
        c = su.enbase(b)
        d = su.debase(c)
        e = su.decode(d)
        assert a == e
        assert b == d
        assert c == su.encode_url(a)
        assert a == su.decode_url(c)


@raises(RuntimeError)
def test_no_ctx():
    su = ShortUrl()
    su.encode(21)
