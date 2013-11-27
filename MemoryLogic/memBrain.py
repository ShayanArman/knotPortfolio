from MemoryModule import mem_cache
from DataStoreModule import UserDB
from RenderModule import handle
from HelperMethods import helper
from StockPricesDB import Stocks

USER_MEMCACHE_KEY = "name"
JSON_MEMCACHE_KEY = "json"
CASH_MEMCACHE_KEY = "cash"

# Set Existing User In Memcache
def setExistingUserInMem(name,json,cash):
	mem_cache.setCashJsonAndName(name,json,cash)

# Set New User In Memcache and Database
def setNewUserInMem(name,password,json,cash):
	UserDB.insertNewUserInDataBase(name,password,json)

def updateUserName(name):
	mem_cache.setMemcache(USER_MEMCACHE_KEY,name)

# Write the list of stocks the user has to the memory and DB
def updateUserStocks(json):
	mem_cache.setMemcache(JSON_MEMCACHE_KEY,json)
	UserDB.updateUserJson(currentUser(),json)

# RETURNS TRUE IF NOT EQUAL TO ZERO. DO NOT PUT NEGATIVE NUM IN THE DB	
# Set the current users cash in memory
def updateCashInMemcacheAndDBAfterSell(cashToAddInteger):
	# First get the current users amount of cash in the memory
	cashString = mem_cache.getCashFromMemcache()
	# Subtract it by how much they just spent
	newCashFloat = float(cashString)+cashToAddInteger
	newCashStr = str(newCashFloat);
	# Set that in the memcache
	mem_cache.setCashInMemcache(newCashStr)
	# Set that in the DB.
	UserDB.updateUserCash(currentUser(),newCashStr)
	# Set that in the DB.
	helper.wait(.1)

# RETURNS TRUE IF NOT EQUAL TO ZERO. DO NOT PUT NEGATIVE NUM IN THE DB	
# Set the current users cash in memory
def updateCashInMemcacheAndDBAfterTransaction(cashToSubtractInteger):
	# First get the current users amount of cash in the memory
	cashString = mem_cache.getCashFromMemcache()
	# Subtract it by how much they just spent
	newCashFloat = float(cashString)-cashToSubtractInteger
	newCashStr = str(newCashFloat);
	# Set that in the memcache
	mem_cache.setCashInMemcache(newCashStr)
	# Set that in the DB.
	UserDB.updateUserCash(currentUser(),newCashStr)
	# Set that in the DB.
	helper.wait(.1)

# // Check to see if there is enough cash for the transaction //
def isThereEnoughCashForTransaction(costInteger):
	# First get the current users amount of cash in the memory
	cashString = mem_cache.getCashFromMemcache()
	# Subtract it by how much they just spent
	newCashFloat = float(cashString)-costInteger
	if(newCashFloat >= 0):
		return True
	else:
		return False

#====== // Get user data \\ ========#
# Return the current users json
def userStocks():
	return mem_cache.getJsonFromMemcache()

# Return the name of the curren user
def currentUser():
	return mem_cache.getUsername()

# Return the users cash.
def userCash():
	return mem_cache.getCashFromMemcache()

#====== // Set stocks in Memcache \\ ========#
def setStocksInMemcache():
	stocksJson = Stocks.getStocks()
	mem_cache.setStockJson(stocksJson)
	
