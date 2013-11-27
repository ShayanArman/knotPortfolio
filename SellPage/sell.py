from RenderModule import handle
from HelperMethods import helper
from MemoryLogic import memBrain
from GetStockPrice import StockOb
from SellStocks import SellStocks
from DataStoreModule import UserDB

# make an object from the json string. Loop through this object, and change each price of the stock to the actual stock.
class SellStocksPage(handle.Handler):
	def get(self,ticker,shares): # A few things to check for. Make sure the stock IS in the DB. AND shares > 0
		username = self.currentUser()
		user = UserDB.getUserByName(username)
		if(shares > 0):
			result = SellStocks.initiateSellingSequenceScotty(ticker,shares,username,user)
			if(result == 'moreSharesThanYouHaveError'):
				self.write('moreSharesThanYouHaveError')
			else:
				self.write(result)
		# # Get the username and redirect to the portfolio
		# redir = '/portfolio/'+username
		# self.redirect(redir)
		