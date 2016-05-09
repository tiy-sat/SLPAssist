from bottle import route, run, template, response, request
import json


@route('/')
@route('/hello')
@route('/hello/<name>')
def index(name="Pardner"):
    return template('<div>Hello, {{person}}!</div>', person=name)



run(host='localhost', port=8080)
