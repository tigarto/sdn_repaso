

#Tomado de: http://www.python.org.ar/wiki/WSGI

# Aqui va mi 'Hola PyAr!, pero con WSGI, una maravilla de Python.

from wsgiref.simple_server import make_server

def hello(environ, start_response):
    start_response('200 OK',[('Content-type','text/plain')])
    return ['Hola PyAr!']

httpd = make_server('',8000, hello).serve_forever()