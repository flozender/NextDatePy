day,month,year = map(int,input("Enter date:").split("-"))

if (year % 400 == 0):
    leap_year = True
elif (year % 100 == 0):
    leap_year = False
elif (year % 4 == 0):
    leap_year = True
else:
    leap_year = False

if (month <= 12):
    if month in (1, 3, 5, 7, 8, 10, 12):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30
else:
    print("Enter date properly")
    
if (day <= 31):
    if day < month_length:
        day += 1
    else:
         day = 1
         if month == 12:
             month = 1
             year += 1
         else:
              month += 1
else:
    print("Enter date properly")
        
print("The next date is %d-%d-%d." % (day, month, year))
if (day,month,year = map(int,input("Enter date:").split("/"))):
    print("The next date is %d-%d-%d." % (day, month, year))
