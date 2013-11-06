#//================================================================================================
import webapp2

from DBUserSavedStocks import SavedUserStocks
from GetStockAndUpdateUserInfo import asyncUpdate
from Login import login
from MainPage import main

#//================================================================================================

app = webapp2.WSGIApplication([('/',login.LoginUser),
                                ('/render/(.*)/(.*)',asyncUpdate.RenderDynamic), # Buy stocks here.
                                ('/portfolio/(.*)', main.MainPage), # Render the main page.
                                ('/renderUserStocksDB',SavedUserStocks.getUserStocks)], debug=True) # Render the users stocks when they log in.