# Import the datetime module and display the current date
import datetime

x = datetime.datetime.now()
print(x)

# The date contains year, month, day, hour, minute, second, and microsecond.
# The datetime module has many methods to return information about the date object.
print(x.year)
print(x.strftime("%A"))

# To create a date, we can use the datetime() class (constructor) of the datetime module.
# The datetime() class requires three parameters to create a date: year, month, day.
y = datetime.datetime(2020, 5, 17)
print(y)
