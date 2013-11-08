from RenderModule import handle
from HelperMethods import helper
from MemoryLogic import memBrain
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
        if(float(price) != 0):
            if(memBrain.isThereEnoughCashForTransaction(cost)):
                memBrain.updateCashInMemcacheAndDBAfterTransaction(cost)
                userStocksString = str(memBrain.userStocks())
                if(userStocksString != 'noStocksBoughtYet'): # If there are stocks, then get the object and add this stock to it.
                    jsonMemoryOb = helper.getJsonObjectFromMemoryString(userStocksString)
                    
                    dictOb = helper.getJsonStockObject(price,ticker,shares)
    
                    dictEmpty = []
                    dictEmpty = jsonMemoryOb
                    dictEmpty.append(dictOb)
    
                    newString = helper.jsonToString(dictEmpty)
                    memBrain.updateUserStocks(newString)
                else: # # If they have no stocks in the DB, make a new stocks object
                    dictString = helper.jsonToString([{'boughtAt':price,'ticker':ticker,'numberOfShares':shares}])
                    memBrain.updateUserStocks(dictString)
    
                self.write(ticker+"~"+price+"~"+shares)
            else:
                self.write('NotEnoughCash')
        else:
            self.write('Error')