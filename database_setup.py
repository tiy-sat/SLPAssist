import psycopg2
import sys
import os
import getpass
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from urllib.parse import urlparse

#connects to heroku or local psql database. 
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
        conn = psycopg2.connect(database='slpassist', user=localuser)

    return conn

def delete_database():
    """Delete the local databse. Only run in dev environment."""

    dbname = "slpassist"
    localuser = getpass.getuser()

    conn = psycopg2.connect(database='postgres', user=localuser)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute('DROP DATABASE IF EXISTS ' + dbname)
    cur.close()
    conn.close()

def create_database():
    """Delete the local databse. Only run in dev environment."""

    dbname = "slpassist"
    localuser = getpass.getuser()

    conn = psycopg2.connect(database='postgres', user=localuser)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute('CREATE DATABASE ' + dbname)
    cur.close()
    conn.close()
