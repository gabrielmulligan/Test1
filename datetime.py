# Solution # 8 26th Mar
# import the datetime function
import datetime
# defined today as current date
today = datetime.datetime.now()
# defined d as the day number for my attempt at working out the text at the end of each day.
d = today.day
# prints the date in the format specified in the problem set
print(today.strftime("%A, %B %d %Y at"),(datetime.time(1).strftime("%I:").lstrip("0")),(today.strftime("%m%p")))

# tried to write code to work out the st or rd or nd at the end of the day number e.g. 23rd, 2nd etc. but wasn't successful.
# This is my attempt below.
# if 4 <= d <= 20 or 24 <= d <= 30:
    # suffix = "th"
# elif d = 1
    # suffix # "st"

# adapted from http://strftime.org/