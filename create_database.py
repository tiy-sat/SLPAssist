import database_setup
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = database_setup.get_connection()
dbname = "slpassist"
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cur.execute('CREATE DATABASE ' + dbname)
cur.close()
con.close()
