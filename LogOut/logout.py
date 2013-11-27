from MemoryModule import mem_cache
from DataStoreModule import UserDB
from RenderModule import handle
from MemoryLogic import memBrain
from StockPricesDB import Stocks

class LogOut(handle.Handler):
    def get(self):
        #Stocks.insertStockStringInDataBase("{'aapl': {'price': '188', 'time': '10-5-6', 'day':'10-5-2012'}}")
        self.logout()
        self.redirect('/')