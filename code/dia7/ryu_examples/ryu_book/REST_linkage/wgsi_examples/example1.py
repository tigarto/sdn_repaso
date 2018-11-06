from webob import Request

def application(environ, start_response):
  start_response('200 OK', [('Content-Type', 'text/html')])
  return ['Hello World!']

req = Request.blank('http://localhost/test')
resp = req.get_response(application)
print resp



