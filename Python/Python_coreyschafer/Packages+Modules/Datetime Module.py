# https://docs.python.org/3/library/datetime.html
# How to work with Dates, Times, Timedeltas, and Timezones

import datetime
from time import CLOCK_UPTIME_RAW
import pytz


# working with datetime.date
d = datetime.date(2016, 7, 21)              # YYYY:MM:DD
print(d)

tday = datetime.date.today()
print(tday)
print(tday.year)        # can also use tday.day, tday.month

print(tday.weekday())                       # Here      Monday => 0      Sunday => 6
print(tday.isoweekday())                    # Here      Monday => 1      Sunday => 7

# time deltas are difference between two dates or times

tdelta = datetime.timedelta(days=7)
print(tdelta)
print(tday + tdelta)


# date2 = date2 + timedelta
# timedelta = date2 - date1 

bday = datetime.date(2021, 12, 22)

till_bday = bday - tday
print(till_bday)            # till_bday.days(), till_bday.total_seconds()







# working with datetime.time 
 
t = datetime.time(9, 12, 54,80)   # HH:MM:SS:ssssss       s=> microseconds      
print(t)                          # t.hour, t.minute, t.seconds





# working with datetime.datetime

dt = datetime.datetime(2021, 6, 8, 12, 4, 30, 30000)     # YYYY:MM:DD:HH:MM:SS:ssssss
print(dt)           # dt.date(), dt.time()
                    # dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second






# using timezones.  pytz

dt_utc = datetime.datetime(2021, 6, 8, 12, 30, 4, tzinfo=pytz.UTC)
print(dt_utc)

dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)

# dt_utcnow1 = datetime.datetime.utcnow()
# dt_utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

# print(dt_utcnow1)
# print(dt_utcnow2)

# to list timezones use pytz.all_timezones
dt_ist = dt_now.astimezone(pytz.timezone('Asia/Calcutta'))
print(dt_ist)

dt_local = datetime.datetime.now()          # Returns local time which is not timezone aware
print( dt_local, ":Naive local datetime")
 
ist_time = pytz.timezone('Asia/Calcutta')
dt_in = ist_time.localize(dt_local)         # now this time is aware of it's timezone
print(dt_in, ":timezone aware local datetime")

# converting onetimezone to other
# here we are converting from Asia/Calcutta  -->  US/Eastern

dt_east = dt_in.astimezone(pytz.timezone('US/Eastern')) 
print(dt_east)



# Different formats of datetime

print(dt_in.isoformat())
formated_date = dt_in.strftime('%B %d, %Y')
print(formated_date)

# have a string convert it to datetime
dt_str = 'June 13, 2021'
dt_from_str = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt_from_str)


# strftime -> Datetime to String
# strptime -> String to Datetime
