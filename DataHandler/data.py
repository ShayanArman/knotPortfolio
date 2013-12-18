from RenderModule import handle

class Data(handle.Handler):
    def get(self):
        self.render("dataPage.html")