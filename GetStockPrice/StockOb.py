from HelperMethods import timeHelp
from HelperMethods import helper
from StockPricesDB import Stocks
from datetime import datetime

DAY = "day"
TIME = "time"

# Class - This class has one purpose. Return the stock price. If it meets the chriteria, return saved price. If not, return 
# Yahoo price.

# M
# This method will return the stock price. 
def getPrice(tick):
	dateTimeArray = timeHelp.makeDayTimeStrings(datetime.utcnow())
	price = cachedStock(tick,dateTimeArray)
	return price

def cachedStock(tick,dateTimeArray):
	today = dateTimeArray[0] #Y-M-D
	currentTime = dateTimeArray[1] #H-M-S
	stocksString = Stocks.getStocks() # stocksString is the string of ALL the stocks.
	stockJsonObject = helper.getJsonObjectFromMemoryString(stocksString) # jstring = {'aapl': {'price': '188', 'time': '10-5-6'}}
	#Get Stock info out of the ticker. So get {'price': '188', 'time': '10-5-6', 'day': '1999-11-03'}
	stockInfo = stockJsonObject.get(tick)
	# If that stock does not exist. A)
	if(stockInfo == None):
		return stockNotInDB(tick,stockJsonObject,today,currentTime)
	else:
		if(isFreshPrice(stockInfo,today,currentTime) == True):
			return float(stockInfo['price']) # return the floating integer price ! 
		else: # if the price is too old. Refresh it.
			return refreshStockPrice(tick,currentTime,today,stockJsonObject)

# Is the time within 15 minutes of the current time?
def isFreshPrice(stockInfo,today,time):
	stockAgeDay = stockInfo['day']
	stockAgeTimeArray = stockInfo['time'].split('-')
	timeArray = time.split('-')

	if(str(stockAgeDay) != str(today)):
		return False
	else:
		minutes = ((float(timeArray[0]) * 60) + float(timeArray[1])) - ((float(stockAgeTimeArray[0]) * 60) + float(stockAgeTimeArray[1]))
		if(minutes <= 15 and minutes > 0):
			return True
		else:
			return False

def wasNotFound(tick):
	return float(helper.priceMe(tick)) #return a floating integer of the price.

# A) Stock not in DB. So ADD it.
# If that specific stock is not in the database,
# Then make a new object with the price, date added, and ticker name. 
# Stuff that object back into the Database for later.
def stockNotInDB(tick, stocksObject, day, time):
	stockPrice = float(helper.priceMe(tick))
	if(stockPrice != 0):
		# make a new price-date-time object. {'aapl': ---->{'day': '1999-11-03', 'time': '10-5-6', 'price': '188'} <--}
		stockPriceDateTime = helper.getJsonDBstockObject(day,time,stockPrice)
		stocksObject[tick] = stockPriceDateTime
		# turn the object into a string in order to save it into the DB
		turnStockObIntoStringAndUpdateDB(stocksObject)
	return stockPrice

# B) # A) Stock not fresh in DB. So REFRESH it.
def refreshStockPrice(tick,currentTime,currentDay,stocksObject):
	stockPrice = float(helper.priceMe(tick))
	if(stockPrice != 0):
		stocksObject.get(tick)['price'] = str(stockPrice)
		stocksObject.get(tick)['day'] = currentDay
		stocksObject.get(tick)['time'] = currentTime
		turnStockObIntoStringAndUpdateDB(stocksObject)
	return stockPrice

# As it says.
def turnStockObIntoStringAndUpdateDB(stockOb):
	# Now that it is updated. Turn the ob into a string to save to DB
	stockString = helper.jsonToString(stockOb)
	# Update the DB
	Stocks.updateStockJson(stockString)






