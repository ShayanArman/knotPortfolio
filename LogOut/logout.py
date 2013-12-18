from RenderModule import handle

class LogOut(handle.Handler):
    def get(self):
        self.logout()
        self.redirect('/')