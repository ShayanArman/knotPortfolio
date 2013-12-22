from RenderModule import handle
from DataStoreModule import UserDB

class BuyHandler(handle.Handler):
    def get(self):
    	name = self.currentUser()
    	if(name):
    		user = UserDB.getUserByName(name)
    		if(user):
    			cash = user.cash
    		else:
    			cash = '100000'
        self.render("buyStocks.html",cash=cash);