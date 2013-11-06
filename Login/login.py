from MemoryModule import mem_cache
from DataStoreModule import UserDB
from RenderModule import handle
from MemoryLogic import memBrain
from StockPricesDB import Stocks


class LoginUser(handle.Handler):
    def get(self):
        self.render("loginPage.html")
    def post(self):
        username = self.request.get('username')
        password = self.request.get('password')
        self.write(username + "| " + password)

        user = UserDB.getUserByName(username)
        if user:
            redir = '/portfolio/' + username
            memBrain.setExistingUserInMem(username,user.json,user.cash)
            self.redirect(redir)
        else:
            memBrain.setNewUserInMem(username,password,'noStocksBoughtYet','100000')
            redir = '/portfolio/' + username
            self.redirect(redir)		