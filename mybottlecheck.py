import os
from bottle import route, run, template, response, request
import json


@route('/')
@route('/hello')
@route('/hello/<name>')
def index(name="Pardner"):
    return template('<div>Hello, {{person}}!</div>', person=name)



run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
