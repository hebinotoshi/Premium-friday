from datetime import date, timedelta

def is_premium_friday(day):
    final = (day.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
    return day.weekday() == 4 and final - day < timedelta(days=7)

def is_premiumer_friday(day):
    return is_premium_friday(day) and day.month % 3 == 0

def is_premiumest_friday(day):
    return is_premium_friday(day) and day.month == 12

def is_premiumerest_friday(day):
    return is_premium_friday(day) and day.month % 6 == 0

def is_all_premiums(day):
    return is_premium_friday(day) and is_premiumer_friday(day) and is_premiumest_friday(day) and is_premiumerest_friday(day)

# Get user input for date, default to today if no input provided
date_str = input("Enter a date (YYYY-MM-DD) or leave blank for today: ")
if not date_str:
    day = date.today()
else:
    year, month, day = map(int, date_str.split("-"))
    day = date(year, month, day)

if is_all_premiums(day):
    print("This date is Premium, Premiumer, Premiumerest, and Premiumest Friday")
elif is_premium_friday(day) and is_premiumer_friday(day) and is_premiumerest_friday(day):
    print("This date is Premium, Premiumer, and Premiumerest Friday")
elif is_premium_friday(day) and is_premiumer_friday(day):
    print("This date is both Premium and Premiumer Friday")
elif is_premium_friday(day) and is_premiumest_friday(day):
    print("This date is both Premium and Premiumest Friday")
elif is_premiumer_friday(day) and is_premiumerest_friday(day):
    print("This date is both Premiumer and Premiumerest Friday")
elif is_premium_friday(day):
    print("This date is Premium Friday")
else:
    print("This date is not a Premium Friday")
