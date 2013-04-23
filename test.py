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
