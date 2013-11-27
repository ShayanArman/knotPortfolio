from MemoryModule import mem_cache
from DataStoreModule import UserDB
from RenderModule import handle
from MemoryLogic import memBrain
from StockPricesDB import Stocks

class Data(handle.Handler):
    def get(self):
        self.render("dataPage.html")