
from time import strftime
import psycopg2

def create_table():
    conn = psycopg2.connect("dbname=jimturbo user=jimturbo")
    cur = conn.cursor()
    cur.execute("""
    CREATE TABLE student
    (
    ID SERIAL PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    parent VARCHAR(100),
    email VARCHAR(250),
    date_added DATE,
    goal VARCHAR
    )
    """)
    conn.commit()
    cur.close()

def delete_table():
    conn = psycopg2.connect('dbname=jimturbo user=jimturbo')
    cur = conn.cursor()
    cur.execute("""
    DELETE FROM student""")
    conn.commit()
    cur.close()

def drop_table():
    conn = psycopg2.connect('dbname=jimturbo user=jimturbo')
    cur = conn.cursor()
    cur.execute("""
    DROP TABLE student""")
    conn.commit()
    cur.close()

def insert_student(aList):
    conn = psycopg2.connect("dbname=jimturbo user=jimturbo")
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO student (first_name,
                         last_name,
                         parent,
                         email,
                         date_added,
                         goal)
          VALUES (%s, %s, %s, %s, %s, %s)""", aList)
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

    print(data)
    studentList = []
    for row in data:
        count = 1
        valDict = {}
        for i in feildList:
            valDict[i] = row[count]
            count += 1
        valDict['date_added'] = valDict['date_added'].strftime('%Y-%m-%d')
        studentList.append(valDict)
    return studentList

aStudent = ['Penny', 'Tool', 'Mamma Tool',
            'mamma.tool@hotmail.com', '2017-01-01', 'roll Rs better']
feildList = ('first_name', 'last_name', 'parent', 'email',
             'date_added', 'goal')
