import csv
import psycopg2


def insert_player(playerList):
    conn = psycopg2.connect("dbname=jimturbo user=jimturbo")
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO student
                (player_name,
                  age,
                  gm_tot,
                  gm_start,
                  min_plyd)
          VALUES (%s, %s, %s, %s, %s)""", playerList)
    conn.commit()
    cur.close()
    conn.close()

def retrieve_students():
    conn = psycopg2.connect("dbname=jimturbo user=jimturbo")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM student""")
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    count = 1
    player_stats = data[0]

    for i in feildList:
        print('{}: {}'.format(i, player_stats[count]))
        count += 1
