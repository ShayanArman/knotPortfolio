import os
import webapp2
import jinja2

# template_dir = os.path.join(os.path.dirname(__file__), 'templates')
# jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

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
    
    def setCookie(self, cookieName, cookieValue):
        self.response.headers.add_header(
            'Set-Cookie', '%s=%s; Path=/' % (cookieName, cookieValue))
    
    def readCookieValue(self, cookieName):
        cookieValue = self.request.cookies.get(cookieName)
        if(cookieValue):
            return cookieValue
        else:
            return None

    def currentUser(self):
        userName = self.request.cookies.get('username')
        if(userName):
            return userName
        return None

    def logout(self):
        self.response.headers.add_header('Set-Cookie', 'username=; Path=/')

    def writeJson(self,user):
        self.redirect('/portfolio/'+user)
    
    def testHandlePY(self,write):
        self.write("handler works: "+write)