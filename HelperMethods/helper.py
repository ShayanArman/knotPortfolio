import ystockquote
import json
import ast
import time

def priceMe(tick):
	price = 0
	try:
		price = float(ystockquote.get_price(tick))
	except:
		return price
	return price

def getJsonObjectFromMemoryString(jstring):
	jsonString = json.dumps(jstring)
	jsonObject = json.loads(jsonString)
	return ast.literal_eval(jsonObject)

def getJsonStockObject(price,tick,shares):
	dictString = json.dumps({'boughtAt':price,'ticker':tick,'numberOfShares':shares})
	return json.loads(dictString)

def jsonToString(jsonObject):
	return json.dumps(jsonObject)

def wait(s):
	time.sleep(s)

# This will be saved in the DB with time and date and price
def getJsonDBstockObject(day,time,price):
	dictString = json.dumps({'day':day,'time':time,'price':price})
	return json.loads(dictString)