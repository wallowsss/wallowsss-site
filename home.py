import cgi
import datetime
import urllib
import wsgiref.handlers
import os
from model import Profile
from model import Services

from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

def servicesMount():
    servicesProfile = ""
    for servicesAll in Services.all():
    	temp = '<a href="%s"><img src="%s" alt="%s" border=0 width=40 height=40 /></a> ' % (servicesAll.link, servicesAll.tumbnail, servicesAll.service)
    	servicesProfile = servicesProfile + temp
    return servicesProfile

class MainPage(webapp.RequestHandler):
    def get(self):
        template_values = {
            'profile': Profile.all(),
            'servicos': servicesMount(),
        }
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

application = webapp.WSGIApplication([
  ('/', MainPage)
], debug=True)


def main():
  run_wsgi_app(application)


if __name__ == '__main__':
  main()

