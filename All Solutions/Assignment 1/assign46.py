#Convert String to Datetime

from datetime import datetime
date = "Aug 26 2021 11:00AM"
datetime = datetime.strptime(date, '%b %d %Y %I : %M%p')
print(type(datetime))
print(datetime)