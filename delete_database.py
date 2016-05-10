import database_setup
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

conn = database_setup.get_connection()
dbname = "slpassist"
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
cur.execute('DROP DATABASE ' + dbname)
conn.commit()
cur.close()
conn.close()
