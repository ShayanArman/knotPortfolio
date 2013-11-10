from RenderModule import handle
from MemoryLogic import memBrain

class MainPage(handle.Handler):
    def get(self,name):
    	cash = memBrain.userCash()
        self.render("MainStockPage.html",cash=cash)