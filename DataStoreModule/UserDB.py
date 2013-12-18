from google.appengine.ext import db

class UserStock(db.Model):
    username = db.StringProperty(required = True)
    password = db.StringProperty(required = True)
    json = db.TextProperty(required = True)
    cash = db.StringProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

    def render(self):
        self.contentWithBreaks = self.content.replace('\n','<br>')
        return render_str("post.html", p = self) 

    def userName(self):
        return self.firstName 

    @classmethod
    def userByName(cls, name):
        user = UserStock.all().filter('username =',name).get()
        return user

def insertNewUserInDataBase(name,pword,json):
    user = UserStock(username=name,password=pword,json=json,cash='100000')
    user.put()

# get user row from database
def getUserByName(name):
    return UserStock.userByName(name)

def updateUserJson(name,data):
    user = getUserByName(name)
    user.json = data
    user.put()

def updateUserCash(name,cash):
    user = getUserByName(name)
    user.cash = cash
    user.put()

def updateUserCashAndJson(name,cash,data):
    user = getUserByName(name)
    user.json = data
    user.cash = cash
    user.put()

def putUser(user):
    user.put()
