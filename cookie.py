import bottle
from beaker.middleware import SessionMiddleware
import os

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.cookie_domain': os.environ.get("COOKIE_DOMAIN", '0.0.0.0'),
    'session.data_dir': './data',
    'session.auto': True
    }

app = SessionMiddleware(bottle.app(), session_opts)
