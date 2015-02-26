import webapp2
from practice.handlers.garages import Garages


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('Hello, webapp World!')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/home', Garages),
    
    ('/garage', Garages),
    ('/garage/(.*)', Garages)
    ], debug=True)
