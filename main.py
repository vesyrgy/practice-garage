import webapp2
from webapp2_extras import jinja2
from practice.handlers.garages import Garages
from practice.handlers.contacts import Contacts
from practice.handlers.home import HomePage
import re


class MainPage(webapp2.RequestHandler):

    def jinja(self):
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **tv):
        """ tv = template value
            add like: a="a", b="c", c={"id": 8240285}
            or
            tv = {"a": "a",  "b":"c", c:{"id": 8240285}}
            **tv
        """
        rv = self.jinja().render_template(_template, **tv)
        self.response.write(rv)

    def get(self):
        self.render_response("index.html")


app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/home', HomePage),
    ('/garages', Garages),
    ('/garages/(.*)/(.*)/(.*)', Garages),
    ('/garages/(.*)/(.*)', Garages),
    ('/garages/(.*)', Garages),
    ('/contacts', Contacts),
    ('/contacts/(.*)/(.*)', Contacts)
    ], debug=True)
