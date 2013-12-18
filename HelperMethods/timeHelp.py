from datetime import datetime

DAY_FORMAT = "%y-%m-%d"
TIME_FORMAT = "%H-%M-%S"
DAY = "day"
TIME = "time"
# Get todays date.
# today = date.today()

def makeDateTimeObjectFromDayString(dayString):
	return datetime.strptime(dayString,DAY_FORMAT)

# def dateStringForDay(todayUTC):
# 	#todayUTC = datetime.utcnow()
# 	return makeStringFromTimeForDay(todayUTC)

# LOGIC
def makeDayTimeStrings(ob):
	dateTimeArray = []
	dateTimeArray.append(ob.strftime(DAY_FORMAT))
	dateTimeArray.append(ob.strftime(TIME_FORMAT))
	return dateTimeArray


# Search for a stock, get the object from the database, and make a json object out of it.
# Read the dictionary with a .get(key,None) call, if it is none, then just hit ystockquote.
# If it is in there, then get the price and the time and date it was added.

# Get todays date as a string by calling timeHelp.dateStringForDay, if that date string is equal to the date on the object,
# Then get the time string.