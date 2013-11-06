from RenderModule import handle

class MainPage(handle.Handler):
    def get(self,name):
        self.render("MainStockPage.html")