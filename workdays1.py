import datetime
import holidays

ONE_DAY = datetime.timedelta(days=1)
HOLIDAYS_US = holidays.US()

def next_business_day():
    next_day = datetime.date.today() + ONE_DAY
    while next_day.weekday() in holidays.WEEKEND or next_day in HOLIDAYS_US:
        next_day += ONE_DAY
        day = str(next_day.day)
        d1 = "/"
        month = str(next_day.month)
        yr = str(next_day.year)
        reformatted = month + d1 + day + d1 + yr
    return reformatted

