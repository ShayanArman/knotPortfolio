#//================================================================================================
import webapp2

from DBUserSavedStocks import SavedUserStocks
from GetStockAndUpdateUserInfo import asyncUpdate
from Login import login
from MainPage import main
from SellPage import sell

#//================================================================================================

app = webapp2.WSGIApplication([('/',login.LoginUser),
                                ('/render/(.*)/(.*)',asyncUpdate.RenderDynamic), # Buy stocks here.
                                ('/portfolio/(.*)', main.MainPage), # Render the main page.
                                ('/renderUserStocksDB',SavedUserStocks.getUserStocks), # Render the users stocks when they log in.
                                ('/sell/(.*)/(.*)', sell.SellStocksPage)], debug=True) # Sell / Ticker / Number Of Shares