from RenderModule import handle
from HelperMethods import helper
from GetStockPrice import StockOb
from DataStoreModule import UserDB
USER_MEMCACHE_KEY = "name"
JSON_MEMCACHE_KEY = "json"
CASH_MEMCACHE_KEY = "cash"

# Buy stocks through this. 
class GetPriceHandler(handle.Handler):
    def get(self,ticker):
        price = str(StockOb.getPrice(ticker))
        if(float(price) != 0):
            self.write(price)
        else:
            self.write('Error')