import webapp2
from practice.handlers.garages import Garages
from practice.handlers.home import HomePage


class MainPage(webapp2.RequestHandler):

    def get(self):
        self.redirect('/home')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/home', HomePage),

    ('/garages', Garages),
    ('/garages/(.*)', Garages)
    ], debug=True)
