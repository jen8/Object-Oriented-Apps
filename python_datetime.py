# http://effbot.org/librarybook/date.htm
# tutorial on datetime module

import datetime

now = datetime.date(2015, 7, 14) # now object have access to all attributes of datetime

print(now.year) # prints 2015
print(now.month) # prints 7


print(datetime.date.today()) # prints today's date, 2017-07-01
print(datetime.date.today().year) # prints 2017
# datetime.date.today() is an object, where we access yr attribute, month attribute. etc

birthdate = datetime.date(1986, 7, 26)

days_old = datetime.date.today() - birthdate # how many days old

print(days_old) 


