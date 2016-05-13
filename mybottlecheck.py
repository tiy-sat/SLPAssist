import os
from bottle import route, run, template, response, request, static_file, get, post, put
import json
import database_setup
import tablefunctions

@route('/')
@route('/login')
def serve_index():
    return static_file('index.html', root='.')

@route('/assets/SLPAssist-logo.png')
def serve_assets():
    return static_file('SLPAssist-logo.png', root='./assets')

@get('/dashboard')
def serve_home():
    return static_file('dashboard.html', root='.')

@post('/students')
def add_students():
    studentData = request.json
    for item in studentData:
        studentlist = [studentData['stuName'],
                       studentData['parEmail'],
                       studentData['parName'],
                       studentData['score']
                       ]
    tablefunctions.insert_student(studentlist)

@post('/users')
def add_users():
    userData = request.json
    #Hash function could be called here
    userList = [userData['slpName'],
                userData['username'],
                userData['slpemail'],
                userData['password'],
                         'slp']

    tablefunctions.insert_user(userList)



@route('/create-account')
def serve_createAccount():
    return static_file('create-account.html', root='.')

@route('/dashboard/settings')
def serve_settings():
    return static_file('settings.html', root='.')

@route('/add-student')
def serve_add_student():
    return static_file('add-student.html', root='.')

@route('/students')
def serve_retrieve_student():
    response.content_type = 'application/json; charset=UTF-8'
    resp_data = tablefunctions.retrieve_students()
    return json.dumps(resp_data)

@post('/students/<id>')
def student_id(id):
    studentData = request.json
    score = studentData['score']
    return tablefunctions.update_score(score=score, student_id=id)

# @code written by Sanketh Katta:
# http://stackoverflow.com/questions/10486224/bottle-static-files/13258941#13258941

#allows dynamic pathing for assets, javascripts, and css files.
@route('<:re:.*/><filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='./js')

@route('<:re:.*/><filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='./styles')

@route('<:re:.*/><filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='./assets')


if __name__ == '__main__':
    if not os.environ.get("DATABASE_URL", None):
        database_setup.delete_database()
        database_setup.create_database()

    tablefunctions.create_table()
    tablefunctions.create_user_table()
    #seeds mock student data.
    astudent = [['Penny Tool', 'Erica Tool', 'nobody@gmail.com', 5],
                ['Jon Yeager', 'Chuck yeager', 'nobody@gmail.com', 3],
                ['Laura Smith', 'Sarah Smith', 'nobody@gmail.com', 7],
                ['Ted Smosby', 'James smosby', 'nobody@gmail.com', 9]]

    auser = ['jimmy', '@admin',  'admin', 'nobody@swbell.net', 'password']

    for row in astudent:
        tablefunctions.insert_student(row)


    tablefunctions.insert_user(auser)

    # Calls to create the tables go here.

    run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
