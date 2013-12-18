from RenderModule import handle
from HelperMethods import helper
from GetStockPrice import StockOb
from DataStoreModule import UserDB
USER_MEMCACHE_KEY = "name"
JSON_MEMCACHE_KEY = "json"
CASH_MEMCACHE_KEY = "cash"

# Buy stocks through this. 
class RenderDynamic(handle.Handler):
    def get(self,ticker,shares):
        price = str(StockOb.getPrice(ticker))
        shares = str(shares)
        cost = (float(price))*(float(shares))
        currentUser = self.currentUser()
        user = UserDB.getUserByName(currentUser)
        if(float(price) != 0 and user):
            newCashFloat = float(user.cash)-cost
            if(newCashFloat >= 0): # is there enough cash
                userStocksString = str(user.json) # get the usersStock json
                if(userStocksString != 'noStocksBoughtYet'): # If there are stocks, then get the object and add this stock to it.
                    jsonMemoryOb = helper.getJsonObjectFromMemoryString(userStocksString)
                    
                    dictOb = helper.getJsonStockObject(price,ticker,shares)
    
                    dictEmpty = []
                    dictEmpty = jsonMemoryOb
                    dictEmpty.append(dictOb)
    
                    newString = helper.jsonToString(dictEmpty)
                    updateDBAfterTransaction(user,str(newCashFloat),newString) #update cash and json for user
                else: # # If they have no stocks in the DB, make a new stocks object
                    dictString = helper.jsonToString([{'boughtAt':price,'ticker':ticker,'numberOfShares':shares}])
                    updateDBAfterTransaction(user,str(newCashFloat),dictString)
                self.write(ticker+"~"+price+"~"+shares)
            else:
                self.write('NotEnoughCash')
        else:
            self.write('Error')

def updateDBAfterTransaction(user,cash,data):
    user.cash = cash
    user.json = data
    UserDB.putUser(user)