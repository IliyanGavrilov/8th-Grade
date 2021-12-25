def valid_year(year):
    return year >= 0

def valid_month(month):
    return month >= 1 and month <= 12

def valid_day(day, month, year):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return day >= 1 and day <= 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return day >= 1 and day <= 30
    elif month == 2 and is_leap(year):
        return day >= 1 and day <= 29
    else:
        return day >= 1 and day <= 28

def valid_hour(hour):
    return hour > 0 and hour < 24

def valid_minute(minute):
    return minute >= 0 and minute < 60

def valid_second(second):
    return second >= 0 and second < 60

def is_leap(year):
    return year % 4 == 0
          
def data_is_valid(year, month, day, hour, minute, second):
    return valid_second(second) and \
        valid_minute(minute) and \
        valid_hour(hour) and \
        valid_day(day, month, year) and \
        valid_month(month) and \
        valid_year(year)

year = int(input("Year = " ))
month = int(input("Month = " ))
day = int(input("Day = "))
hour = int(input("Hour = " ))
minute = int(input("Minute = " ))
second = int(input("Second = " ))	
print(data_is_valid(year, month, day, hour, minute, second))	