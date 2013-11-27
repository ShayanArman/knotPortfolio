from RenderModule import handle
from HelperMethods import helper
from MemoryLogic import memBrain
from GetStockPrice import StockOb
from DataStoreModule import UserDB
USER_MEMCACHE_KEY = "name"
JSON_MEMCACHE_KEY = "json"
CASH_MEMCACHE_KEY = "cash"

# =============================================================

def initiateSellingSequenceScotty(tick,shares,name,user):
	numberOfSharesForStock = 0
	tick = tick.upper()
	userStocksString = str(user.json)
	cash = float(user.cash)
	if(userStocksString != 'noStocksBoughtYet'): # If there are stocks, then get the object and add this stock to it.
		jsonMemoryOb = helper.getJsonObjectFromMemoryString(userStocksString)
		for ob in jsonMemoryOb:
			if(ob['ticker'] == tick):
				numberOfSharesForStock += int(ob['numberOfShares'])
	if(float(shares) > numberOfSharesForStock):
		return "moreSharesThanYouHaveError" # trying to sell more shares than you have
	else:
		if(float(shares) == numberOfSharesForStock):
			sellingPrice = sellAllTheShares(tick,shares,jsonMemoryOb,cash,user)
		else:
			sellingPrice = sellSomeShares(tick,shares,jsonMemoryOb,cash,user)
	return sellingPrice

# Selling all the shares
# Calculate the selling price. Take the sale price and subtract the commission.
# Remove the stock from the stockInfo.json
# take the proceeds, and add it to shayan's info. ie. increase the cash holding. 
# Show them how much cash they have.
def sellAllTheShares(tick,shares,data,cash,user):
	sellingPrice = StockOb.getPrice(tick)
	if(sellingPrice != 0):
		mississipiMoney = (sellingPrice * float(shares))
		cash += mississipiMoney # Subtract the commission eventually
		user.cash = str(cash)
		removeObjectFromData(tick,data,user)
	return mississipiMoney

def sellSomeShares(tick,shares,data,cash,user):
	sellingPrice = StockOb.getPrice(tick) # Could return zero.
	if(sellingPrice != 0):
		mississipiMoney = (sellingPrice * float(shares))
		cash += mississipiMoney # Subtract the price for selling a stock - Commission.
		user.cash = str(cash)
		removePartsOfObjectFromData(tick,shares,data,user)
	return mississipiMoney

# Sell ALL the shares of a stock.
def removeObjectFromData(ticker,data,user):
	listLength = int(len(data))
	counter = 0
	for x in range(0,listLength):
		ob = data[counter]
		if(ob['ticker'] == ticker):
			data.pop(counter)
		else:
			counter += 1
	newString = helper.jsonToString(data)
	updateDBAfterTransaction(user,newString)

# Only sell a few shares of the stock.
def removePartsOfObjectFromData(ticker,shares,data,user):
	sellShares = int(shares)
	listLength = int(len(data))
	counter = 0
	for x in range(0,listLength):
		ob = data[counter]
		if(sellShares == 0):
			break
		if(ob['ticker'] == ticker):
			obShares = int(ob['numberOfShares'])
			if(obShares <= sellShares):
				data.pop(counter)
				sellShares -= obShares
			else:
				data[counter]['numberOfShares'] = str(obShares - sellShares)
				sellShares = 0
		else:
			counter += 1
	newString = helper.jsonToString(data)
	updateDBAfterTransaction(user,newString)

def updateDBAfterTransaction(user,data):
    user.json = data
    UserDB.putUser(user)