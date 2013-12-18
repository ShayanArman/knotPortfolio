from RenderModule import handle

class SellHandler(handle.Handler):
    def get(self):
        self.render("sellStocks.html");