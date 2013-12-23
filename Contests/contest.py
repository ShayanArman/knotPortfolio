from RenderModule import handle

class ContestPage(handle.Handler):
    def get(self):
        self.render("contests.html")