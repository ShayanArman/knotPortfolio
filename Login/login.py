from DataStoreModule import UserDB
from RenderModule import handle
#from StockPricesDB import Stocks

def isCorrectUser(dbPassword,password):
    if(dbPassword == password):
        return True
    return False
    
class LoginUser(handle.Handler):
    def get(self):
        #Stocks.insertStockStringInDataBase("{'aapl': {'price': '188', 'time': '10-5-6', 'day':'10-5-2012'}}")
        username = self.currentUser()
        user = UserDB.getUserByName(str(username))
        if user:
            redir = '/portfolio/' + username
            self.redirect(redir)
        else:
            self.render("loginPage.html")
    def post(self):
        username = self.request.get('username')
        username = username.lower()
        password = self.request.get('password')

        user = UserDB.getUserByName(username) # if user is in the database. either correct password or not.
        # if correct password do this.
        if user:
            if isCorrectUser(user.password,password):
                redir = '/portfolio/' + username
                self.setCookie('username',str(username))
                self.redirect(redir)
            else:
                self.redirect('/')
        else:
            self.redirect('/register')