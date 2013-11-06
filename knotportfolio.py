#//================================================================================================
import webapp2

from DBUserSavedStocks import SavedUserStocks
from GetStockAndUpdateUserInfo import asyncUpdate
from Login import login
from MainPage import main

#//================================================================================================

app = webapp2.WSGIApplication([('/',login.LoginUser),
                                ('/render/(.*)/(.*)',asyncUpdate.RenderDynamic),
                                ('/portfolio/(.*)', main.MainPage),
                                ('/renderUserStocksDB',SavedUserStocks.getUserStocks)], debug=True)