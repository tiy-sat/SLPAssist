
from time import strftime
import psycopg2
import json

def create_table():
    conn = psycopg2.connect("dbname=slpassist user=localuser")
    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS students""")
    cur.execute("""
    CREATE TABLE students
    (
    ID SERIAL PRIMARY KEY,
    stuFirst VARCHAR(50),
    stuLast VARCHAR(50),
    parFirst VARCHAR(50),
    parLast VARCHAR(50),
    email VARCHAR(250),
    dateAdded DATE
    )
    """)
    conn.commit()
    cur.close()

def delete_table():
    conn = psycopg2.connect('dbname=slpassist user=localuser')
    cur = conn.cursor()
    cur.execute("""
    DELETE FROM students""")
    conn.commit()
    cur.close()

def drop_table():
    conn = psycopg2.connect('dbname=slpassist user=localuser')
    cur = conn.cursor()
    cur.execute("""
    DROP TABLE students""")
    conn.commit()
    cur.close()

def insert_student(aList):
    conn = psycopg2.connect("dbname=slpassist user=localuser")
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO students (stuFirst,
                         stuLast,
                         parFirst,
                         parLast,
                         email,
                         dateAdded)
          VALUES (%s, %s, %s, %s, %s, %s)""", aList)
    conn.commit()
    cur.close()
    conn.close()

def retrieve_students():
    conn = psycopg2.connect("dbname=slpassist user=localuser")
    cur = conn.cursor()
    cur.execute("""SELECT * FROM students""")
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    print(data)
    studentList = []
    for row in data:
        count = 1
        valDict = {}
        for i in keyList:
            valDict[i] = row[count]
            count += 1
        valDict['dateAdded'] = valDict['dateAdded'].strftime('%Y-%m-%d')
        studentList.append(valDict)
    return json.dumps(studentList)

# test list
aStudent = ['Penny', 'Tool', 'Mamma', 'Tool',
            'mamma.tool@hotmail.com', '2017-01-01']
# list containing key names
keyList = ('stuFirst', 'stuLast', 'parFirst', 'parLast', 'email',
             'dateAdded')
