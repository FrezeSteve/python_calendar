"""
store date data in timedelta
"""
from calendar import monthrange, month_name
from datetime import datetime

today = datetime.now()
datetime_object = {
    "year": today.year,
    "current_month": today.month,
    "number_of_months": 12,
}
for i in range(datetime_object['current_month'], datetime_object['number_of_months'] + 1):
    number_of_months = monthrange(datetime_object['year'], i)[1]
    month = month_name[i]
    print(number_of_months, "%s" % month)
