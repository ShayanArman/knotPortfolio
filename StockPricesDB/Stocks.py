from google.appengine.ext import db

STOCK_KEY = 'stockJSON'
class Stocks(db.Model):
    keyName = db.StringProperty(required = True)
    savedStocks = db.TextProperty(required = True)
    created = db.DateTimeProperty(auto_now_add = True)

    @classmethod
    def stockByKey(cls, key):
        stocks = Stocks.all().filter('keyName =',key).get()
        return stocks

def insertStockStringInDataBase(stocksString):
    stocks = Stocks(keyName=STOCK_KEY,savedStocks=stocksString)
    stocks.put()

def updateStockJson(stockJsonString):
    stocks = getStocksRow()
    stocks.savedStocks = stockJsonString
    stocks.put()

# get user row from database
def getStocksRow():
    return Stocks.stockByKey(STOCK_KEY)

def getStocks():
    return getStocksRow().savedStocks

# What does it look like brotha?
# jstring = {'aapl': {'price': '188', 'time': '10-5-6'}}
# jstring = json.loads(jstring)
# job = json.dumps(jstring)
# how do i get it? job.get("aapl") == None: print didn't find it.