from RenderModule import handle
from HelperMethods import helper
from MemoryLogic import memBrain
from GetStockPrice import StockOb

# make an object from the json string. Loop through this object, and change each price of the stock to the actual stock.
class getUserStocks(handle.Handler):
	def get(self):
		jsonString = memBrain.userStocks()
		if(str(jsonString) != 'noStocksBoughtYet'):
			stocksDict = helper.getJsonObjectFromMemoryString(jsonString)
			for ob in stocksDict:
				# THIS IS THE FAST CODE ob['currentPrice'] = helper.priceMe(str(ob['ticker']))
				ob['currentPrice'] = StockOb.getPrice(str(ob['ticker']))
				helper.wait(.2)
			stocksString = helper.jsonToString(stocksDict)
			self.write(stocksString)
		else:
			self.write('Empty')