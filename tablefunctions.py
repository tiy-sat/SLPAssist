from time import strftime
import psycopg2
import json
from database_setup import get_connection

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS students""")
    cur.execute("""
    CREATE TABLE students
    (
    ID SERIAL PRIMARY KEY,
    stuName VARCHAR(100),
    parName VARCHAR(100),
    parEmail VARCHAR(250),
    score SMALlINT
    )
    """)
    conn.commit()
    cur.close()

def create_user_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""DROP TABLE IF EXISTS users""")
    cur.execute("""
    CREATE TABLE users
    (
     ID Serial Primary Key,
     slpName VARCHAR(100),
     username VARCHAR(100),
     slpemail VARCHAR(255),
     type VARCHAR(100),
     password VARCHAR(255)
    )
    """)
    conn.commit()
    cur.close()

def delete_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    DELETE FROM students""")
    conn.commit()
    cur.close()

def drop_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    DROP TABLE students""")
    conn.commit()
    cur.close()

def insert_student(aList):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO students(stuName,
                         parName,
                         parEmail,
                         score)
          VALUES (%s, %s, %s, %s)""", aList)
    conn.commit()
    cur.close()
    conn.close()

def insert_user(aList):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    INSERT INTO users(slpName,
                      username,
                      type,
                      slpemail,
                      password)
         Values (%s, %s, %s, %s, %s)""", aList)
    conn.commit()
    cur.close()
    conn.close()

def update_score(student_id, score):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
    UPDATE students
    set score= %s
    where id= %s""", (score, student_id))
    conn.commit()
    cur.close()
    conn.close()


def retrieve_students():
    keyList = ('id', 'stuName', 'parName', 'parEmail', 'score')
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""SELECT * FROM students""")
    data = cur.fetchall()
    conn.commit()
    cur.close()
    conn.close()

    studentList = []
    for row in data:
        count = 0
        valDict = {}
        for i in keyList:
            valDict[i] = row[count]
            count += 1
        # valDict['dateAdded'] = valDict['dateAdded'].strftime('%Y-%m-%d')
        studentList.append(valDict)
    return studentList

# test student
# aStudent = ['Penny Tool', 'Mamma Tool', 8]


# test student
# aStudent = ['Penny Tool', 'Mamma Tool', 8]
