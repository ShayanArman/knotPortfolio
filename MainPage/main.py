from RenderModule import handle
from MemoryLogic import memBrain
from DataStoreModule import UserDB

class MainPage(handle.Handler):
    def get(self,name):
    	username = self.currentUser()
    	if(name == username):
    		user = UserDB.getUserByName(username)
    		if(user):
    			cash = user.cash
    		else:
    			cash = '100000'
        	self.render("portfolio.html",cash=cash)
        else:
        	self.redirect('/')