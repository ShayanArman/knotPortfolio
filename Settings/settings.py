from RenderModule import handle

class Settings(handle.Handler):
    def get(self):
        self.render("settings.html")