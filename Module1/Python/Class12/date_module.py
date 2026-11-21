import datetime 
from datetime import datetime as dt


now = datetime.datetime.now()
print(now)

print(now.time())
print(now.date())
print(now.date().year)


print(now.date().weekday())

# Formatting dates
print(now.strftime('%d-%m-%Y'))
print(now.strftime('%d-%M-%y'))
print(now.strftime('%d-%b-%y'))
print(now.strftime('%d-%B-%y'))

# Date Creation
dob = dt(2003,8,8)
print(dob)

# DATE OPERATIONS

date = dt.now()
print((date - dob).days)


