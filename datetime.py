import datetime
today = datetime.date.today()
yesterday = today - datetime.timedelta(days = 1)
Tomorrow = today + datetime.timedelta(days = 1)
print("Yesterday : ",yesterday)
print("TOday : ", today)
print("Tomorrow : ",Tomorrow)