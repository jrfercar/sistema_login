import os
from bottle import Bottle, route
from bottle import run, request
from bottle import template, post
from bottle import view, static_file
from bottle import get, error

'''
@route('/')
def index():
	return '<h1>Hello world</h1>'

if __name__ == '__main__':
	run(host='localhost', port=8080, debug=True)

@route('/')
@route('/user/<nome>')
def index(nome='Desconhecido'):
    return '<center><h1>Olá ' + nome + '</h1></center>'

@route('/python')
def python():
    return '<h1>Curso de Python</h1>'

@route('/artigo/<id>')
def artigo(id):
    return '<h1>Você está lendo o artigo ' + id + '</h1>'

@route('/pagina/<id>/<nome>')
def pagina(id, nome):
    return '<h1>Você está vendo a página ' + id + ' com o nome ' + nome + '</h1>'
'''

# static routes
@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')

@get('/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='static/js')

@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')

@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')

'''
@route('/')
def index():
    return template('index')
'''

@route('/')#@get('/login')
def login():
    return template('login')

def checkLogin(username, password):
    d = {'marcos':'python', 'joao':'java', 'pedro':'go'}

    return True if username in d.keys() and d[username] == password else False

@route('/', method='POST') #@post('/login')
def acaoLogin():
    username=request.forms.get('username')
    password=request.forms.get('password')

    return template('verificacao_login', sucesso = checkLogin(username, password), nome=username)

@error(404)
def error404(error):
    return template('pagina404')
    
if __name__ == '__main__':
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    else:
        run(host='localhost', port=8080, debug=True, reloader=True)
        
