from MemoryModule import mem_cache
from DataStoreModule import UserDB
from RenderModule import handle
from MemoryLogic import memBrain
from StockPricesDB import Stocks

class BuyHandler(handle.Handler):
    def get(self):
        self.render("buyStocks.html");