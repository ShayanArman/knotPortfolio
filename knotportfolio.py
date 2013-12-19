#//================================================================================================
import webapp2

from DBUserSavedStocks import SavedUserStocks
from GetStockAndUpdateUserInfo import asyncUpdate
from Login import login
from MainPage import main
from SellPage import sell
from LogOut import logout
from BuyStocksHandler import buyHandler
from SellStocksHandler import sellHandler
from DataHandler import data
from Settings import settings
from GetStockPrice import stockPriceHandler

#//================================================================================================

app = webapp2.WSGIApplication([('/',login.LoginUser),
                                ('/render/(.*)/(.*)',asyncUpdate.RenderDynamic), # Buy stocks here.
                                ('/portfolio/(.*)', main.MainPage), # Render the main page.
                                ('/renderUserStocksDB',SavedUserStocks.getUserStocks), # Render the users stocks when they log in.
                                ('/sell/(.*)/(.*)', sell.SellStocksPage),
                                ('/logout', logout.LogOut),
                                ('/settings', settings.Settings),
                                ('/getPrice/(.*)', stockPriceHandler.GetPriceHandler),
                                ('/data', data.Data),
                                ('/buystocks', buyHandler.BuyHandler),
                                ('/sellstocks',sellHandler.SellHandler)], debug=True) # Sell / Ticker / Number Of Shares