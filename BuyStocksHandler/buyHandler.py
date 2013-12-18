from RenderModule import handle

class BuyHandler(handle.Handler):
    def get(self):
        self.render("buyStocks.html");