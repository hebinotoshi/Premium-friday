from datetime import date, timedelta

def is_last_friday():
    today = date.today()
    last_day_of_month = today.replace(day=28) + timedelta(days=4)  # add 4 days to get to the last day of the month
    if today.month != last_day_of_month.month:
        last_day_of_month = last_day_of_month.replace(day=1)  # if the last day is in the next month, set it to the first day of the next month
    days_until_last_friday = (last_day_of_month - today).days
    return days_until_last_friday == 0 and today.weekday() == 4  # 4 is Friday

