# DO NOT SELL THIS AS YOUR OWN, OR ANY OF MY GARBAGE!! GO LEARN TO CODE LMAO

Settings = {
    "Year": 2050, #What year to stop at
    "HaveLimit": True, #If your gonna have a limit
    "Limit": 250, #About 100 years worth
}

import datetime
from datetime import date
from datetime import datetime as t
from datetime import timedelta as td

isfriday13 = False
fridate = date.today()
days = []
daycount = 0
while isfriday13 == False:
    dr = fridate + td(days=1)
    fridate = dr
    if int(dr.day) == 13:
        if int(dr.isoweekday()) == 5:
            if int(dr.year) < Settings["Year"]:
                if Settings["HaveLimit"] == True:
                    if daycount < Settings["Limit"]:
                        daycount += 1
                        days.append(["Day: "+str(daycount),str(dr.day)+"/"+str(dr.month)+"/"+str(dr.year)])
                else:
                    daycount += 1
                    days.append(["Day: "+str(daycount),str(dr.day)+"/"+str(dr.month)+"/"+str(dr.year)])
            else:
                isfriday13 = True
                print(days)
