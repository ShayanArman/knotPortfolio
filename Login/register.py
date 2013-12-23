from DataStoreModule import UserDB
from RenderModule import handle

def isCorrectUser(dbPassword,password):
    if(dbPassword == password):
        return True
    return False
    
class RegisterUser(handle.Handler):
    def get(self):
        self.render("registerPage.html")
    def post(self):
        username = self.request.get('username')
        username = username.lower()
        password = self.request.get('password')

        user = UserDB.getUserByName(username) # if user is in the database. either correct password or not.
        if(user):
            self.redirect('/')
        else:
            self.setCookie('username',str(username))
            UserDB.insertNewUserInDataBase(username,password,'noStocksBoughtYet')
            redir = '/portfolio/' + username
            self.redirect(redir)		