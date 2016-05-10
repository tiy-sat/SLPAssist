import psycopg2
import sys
import os
import getpass
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from urllib.parse import urlparse

def get_connection():
    localuser = getpass.getuser()
    db_url = os.environ.get("DATABASE_URL", None)
    conn = None
    if db_url:
        url = urlparse(db_url)
        conn = psycopg2.connect(
            database=url.path[1:],
            user=url.username,
            password=url.password,
            host=url.hostname,
            port=url.port)

    else:
        conn = psycopg2.connect("dbname=slpassist user={}".format(localuser))
    return conn
