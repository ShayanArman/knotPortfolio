import os
import re
import sys
import webapp2
import jinja2

from string import letters
from google.appengine.ext import db
from datetime import timedelta, datetime
from google.appengine.api import memcache

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

jinja_environment = jinja2.Environment(loader=jinja2.FileSystemLoader(['templates', 'templates\css']));

class Handler(webapp2.RequestHandler):
    # Instead of having to write self.response.out.write everytime.
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)
    # First get the template that's passed in from templates directory.
    # Then write out the template and fill out the parameters with the variables passed in.
    def render(self, template, **params):
        emptyTemplate = jinja_environment.get_template(template)
        self.write(emptyTemplate.render(params))
    def writeJson(self,user):
        self.redirect('/portfolio/'+user)
    def testHandlePY(self,write):
        self.write("handler works: "+write)