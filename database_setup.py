import psycopg2
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


con = psycopg2.connect("user=davidvillarreal user=davidvillarreal")
dbname = "slpassist"
con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = con.cursor()
cur.execute('CREATE DATABASE ' + dbname)
cur.close()
con.close()
