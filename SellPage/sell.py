from RenderModule import handle
from HelperMethods import helper
from MemoryLogic import memBrain
from GetStockPrice import StockOb
from SellStocks import SellStocks

# make an object from the json string. Loop through this object, and change each price of the stock to the actual stock.
class SellStocksPage(handle.Handler):
	def get(self,ticker,shares): # A few things to check for. Make sure the stock IS in the DB. AND shares > 0
		if(shares > 0):
			SellStocks.initiateSellingSequenceScotty(ticker,shares)
		# Get the username and redirect to the portfolio
		username = str(memBrain.currentUser())
		redir = '/portfolio/'+username
		self.redirect(redir)
		