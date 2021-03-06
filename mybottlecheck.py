import os
from bottle import route, run, template, response, request, static_file, get, post, put
import json
import database_setup
import tablefunctions
from passlib.hash import sha512_crypt
from beaker.middleware import SessionMiddleware


# Web functions
@route('/')
def serve_index():
    return static_file('index.html', root='.')

@route('/login_page')
def serve_login_page():
    return static_file('login.html', root='.')

@route('/create-account')
def serve_add_student():
    return static_file('create-account.html', root='.')

@route('/styles/main.css')
def serve_css():
    return static_file('main.css', root='./styles')

@route('/assets/SLPAssist-logo.png')
def serve_assets():
    return static_file('SLPAssist-logo.png', root='./assets')

@get('/dashboard')
def serve_home():
    return static_file('dashboard.html', root='.')

@route('/dashboard/settings')
def serve_settings():
    return static_file('settings.html', root='.')

@route('/add-student')
def serve_add_student():
    return static_file('add-student.html', root='.')

# API functions
@route('/students')
def serve_retrieve_student():
    response.content_type = 'application/json; charset=UTF-8'
    resp_data = tablefunctions.retrieve_students()
    return json.dumps(resp_data)

<<<<<<< HEAD
# API functions
=======
>>>>>>> b5fe5d09d48778d344f86cbba721e0cb2759f085
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

<<<<<<< HEAD
=======
@post('/users')
def add_users():
    userData = request.json
    #Hash function could be called here
    userList = [userData['slpName'],
                userData['userName'],
                userData['slpEmail'],
                               'slp',
                userData['password']]

    tablefunctions.insert_user(userList)

>>>>>>> b5fe5d09d48778d344f86cbba721e0cb2759f085
@post('/students/<id>')
def student_id(id):
    studentData = request.json
    score = studentData['score']
    return tablefunctions.update_score(score=score, student_id=id)

#########################################################
@post('/login')
def do_login():
    # bottle.request.environ.get('beaker.session')
    username = request.forms.get('username')
    password = request.forms.get('password')
    if tablefunctions.retrieve_password(username) == None:
        return "<p>Username or password is not correct.</p>"
    elif sha512_crypt.verify(password, tablefunctions.retrieve_password(username)):
        # s['user_id'] = True
        # response.set_cookie("account", username, secret='some-secret-key')
        # s.save()
        return serve_home()
    else:
        return "<p>Username or password is not correct.</p>"

 @post('/logout')
 def log_user_out():
     s = bottle.request.environ.get('beaker.session')
     del s['user_id']
     s.save()
#########################################################

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

    auser = ['Bruce Springsteen', 'theboss', 'nobody@swbell.net', 'admin', 'estreet']

    for row in astudent:
        tablefunctions.insert_student(row)


    tablefunctions.insert_user(auser)

    # Calls to create the tables go here.

    run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
