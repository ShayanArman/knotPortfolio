from RenderModule import handle
from HelperMethods import helper
from MemoryLogic import memBrain
from GetStockPrice import StockOb
from DataStoreModule import UserDB
USER_MEMCACHE_KEY = "name"
JSON_MEMCACHE_KEY = "json"
CASH_MEMCACHE_KEY = "cash"
# 
class RenderDynamic(handle.Handler):
    def get(self,ticker,shares):
        price = str(StockOb.getPrice(ticker))
        shares = str(shares)
        cost = (float(price))*(float(shares))
        if(float(price) != 0):
            print('helloShayan!!!helloShayan!!!helloShayan!!!helloShayan!!!helloShayan!!!helloShayan!!!')
            if(memBrain.isThereEnoughCashForTransaction(cost)):
                memBrain.updateCashInMemcacheAndDBAfterTransaction(cost)
                userStocksString = str(memBrain.userStocks())
                if(userStocksString != 'noStocksBoughtYet'):
                    jsonMemoryOb = helper.getJsonObjectFromMemoryString(userStocksString)
                    
                    dictOb = helper.getJsonStockObject(price,ticker,shares)
    
                    dictEmpty = []
                    dictEmpty = jsonMemoryOb
                    dictEmpty.append(dictOb)
    
                    newString = helper.jsonToString(dictEmpty)
                    memBrain.updateUserStocks(newString)
                else:
                    dictString = helper.jsonToString([{'boughtAt':price,'ticker':ticker,'numberOfShares':shares}])
                    memBrain.updateUserStocks(dictString)
    
                self.write(ticker+"~"+price+"~"+shares)
            else:
                self.write('NotEnoughCash')
        else:
            self.write('Error')