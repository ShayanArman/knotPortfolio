# from google.appengine.ext import db
from google.appengine.api import memcache

USER_MEMCACHE_KEY  = "name"
JSON_MEMCACHE_KEY  = "json"
CASH_MEMCACHE_KEY  = "cash"
STOCK_MEMCACHE_KEY = "stocks"


# #====== // Username Methods \\ =====#
# def setUsernameInMemcache(name):
#     memcache.set(USER_MEMCACHE_KEY, name)

# def getUsername():
#     name = memcache.get(USER_MEMCACHE_KEY)
#     if name:
#         return name
#     else:
#         self.redirect('/')

# #====== // JSON methods ===========#
# def setJsonInMemcache(data):
# 	memcache.set(JSON_MEMCACHE_KEY,data)

# def getJsonFromMemcache():
#     return memcache.get(JSON_MEMCACHE_KEY)

# #======== // Cash methods \\ ========#
# def setCashInMemcache(cash):
# 	memcache.set(CASH_MEMCACHE_KEY,cash)

# def getCashFromMemcache():
# 	return memcache.get(CASH_MEMCACHE_KEY)


# #==== // General Memcache \\ =======#
# def setMemcache(switch,data):
# 	if(switch == USER_MEMCACHE_KEY):
# 		setUsernameInMemcache(data)
# 	elif (switch == JSON_MEMCACHE_KEY):
# 		setJsonInMemcache(data)
# 	else:
# 		setCashInMemcache(data)

# def setCashJsonAndName(name,json,cash):
# 	setMemcache(USER_MEMCACHE_KEY,name)
# 	setMemcache(JSON_MEMCACHE_KEY,json)
# 	setMemcache(CASH_MEMCACHE_KEY,cash)

#====== // Stock DB Methods \\ ======#
def setStockJson(stocks):
	memcache.set(STOCK_MEMCACHE_KEY, stocks)

def getStockJson():
	return memcache.get(STOCK_MEMCACHE_KEY)
