import os
from bottle import route, run, template, response, request, static_file
import json
import database_setup


@route('/')
@route('/login')
def serve_index():
    return static_file('index.html', root='.')

@route('/styles/main.css')
def serve_css():
    return static_file('main.css', root='./styles')

@route('/hello')
@route('/hello/<name>')
def index(name="Pardner"):
    return template('<div>Howdy, {{person}}!</div>', person=name)


@route('/dashboard.html')
def serve_home():
    return static_file('dashboard.html', root='.')

@route('/add-student.html')
    return static_file('add-student.html', root='.')

if __name__ == '__main__':
    if not os.environ.get("DATABASE_URL", None):
        database_setup.delete_database()
        database_setup.create_database()

    # Calls to create the tables go here.

    run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)), debug=True)
