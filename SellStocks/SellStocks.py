from RenderModule import handle
from HelperMethods import helper
from MemoryLogic import memBrain
from GetStockPrice import StockOb
from DataStoreModule import UserDB
USER_MEMCACHE_KEY = "name"
JSON_MEMCACHE_KEY = "json"
CASH_MEMCACHE_KEY = "cash"

# =============================================================

def initiateSellingSequenceScotty(tick,shares):
	numberOfSharesForStock = 0
	userStocksString = str(memBrain.userStocks())
	tick = tick.upper()
	if(userStocksString != 'noStocksBoughtYet'): # If there are stocks, then get the object and add this stock to it.
		jsonMemoryOb = helper.getJsonObjectFromMemoryString(userStocksString)
		for ob in jsonMemoryOb:
			if(ob['ticker'] == tick):
				numberOfSharesForStock += int(ob['numberOfShares'])
	print "NUMBER OF SHARES " + str(numberOfSharesForStock)
	if(float(shares) > numberOfSharesForStock):
		return "moreSharesThanYouHaveError" # trying to sell more shares than you have
	else:
		if(float(shares) == numberOfSharesForStock):
			print "SHAYAN number of shares is equal"
			sellAllTheShares(tick,shares,jsonMemoryOb)
		else:
			sellSomeShares(tick,shares,jsonMemoryOb)

# Selling all the shares
# Calculate the selling price. Take the sale price and subtract the commission.
# Remove the stock from the stockInfo.json
# take the proceeds, and add it to shayan's info. ie. increase the cash holding. 
# Show them how much cash they have.
def sellAllTheShares(tick,shares,data):
	sellingPrice = StockOb.getPrice(tick)
	moneyMade = (sellingPrice * float(shares)) # Subtract the commission eventually
	memBrain.updateCashInMemcacheAndDBAfterSell(moneyMade)
	removeObjectFromData(tick,data)

def sellSomeShares(tick,shares,data):
	sellingPrice = StockOb.getPrice(tick) # Could return zero.
	if(sellingPrice != 0):
		mississipiMoney = (sellingPrice * float(shares)) # Subtract the price for selling a stock - Commission.
		memBrain.updateCashInMemcacheAndDBAfterSell(mississipiMoney)
		removePartsOfObjectFromData(tick,shares,data)

# Sell ALL the shares of a stock.
def removeObjectFromData(ticker,data):
	listLength = int(len(data))
	counter = 0
	for x in range(0,listLength):
		ob = data[counter]
		if(ob['ticker'] == ticker):
			data.pop(counter)
		else:
			counter += 1
	newString = helper.jsonToString(data)
	memBrain.updateUserStocks(newString)

# Only sell a few shares of the stock.
def removePartsOfObjectFromData(ticker,shares,data):
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
	memBrain.updateUserStocks(newString)
                 



