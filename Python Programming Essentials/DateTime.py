import datetime
def days_in_month(year, month):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month
      
    Returns:
      The number of days in the input month.
    """
    a = False
    if year % 4 == 0:
        a = True
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        if a == True:
            return 29
        else:
            return 28
    else:
        return 30
def is_valid_date(year, month, day):
    """
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day
      
    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    total_days = days_in_month(year, month)
    if day > total_days or day <=0 or month > 12 or month <=0 or year <= 0:
        return False
    else:
        return True
     
def days_between(year1, month1, day1, year2, month2, day2):
    """
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date
      
    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is 
      before the first date.
    """
    if not (is_valid_date(year1, month1, day1)) or not(is_valid_date(year2, month2, day2)):
        return 0
    if year2 < year1 or (year1 == year2 and month2 < month1) or   (year1 == year2 and month2 == month1 and day2 < day1):
        return 0
    total_days = 0
    
    if year1 == year2 and month1 == month2:
        return day2 - day1
    elif year1 == year2:
        temp = month1 + 1
        day_temp = days_in_month(year1, month1)
        total_days += (day_temp - day1)
        total_days += day2
        while temp < month2:
            total_days += days_in_month(year1, temp)
            temp += 1
        return total_days
    else:
        temp = month1 + 1
       
        day_temp = days_in_month(year1, month1)
        total_days += (day_temp - day1)
        total_days += day2
        if temp == 13:
            temp = 1
            year1 += 1
        while temp != month2 or year1 != year2:
            total_days += days_in_month(year1, temp)
            temp += 1
            if temp == 13:
                temp = 1
                year1 += 1
        return total_days

def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day
      
    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    extra = 0
    if year == 1:
        extra = 15
    today = datetime.date.today()
    today = str(today)
    li = today.split("-")
    today_day = int(li[2])
    today_month = int(li[1])
    today_year = int(li[0])
    total_days_in_birthday = days_between(year, month,  day, today_year, today_month, today_day)
    return total_days_in_birthday - extra
 
