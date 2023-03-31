from datetime import datetime, timedelta

def is_premium_friday(day):
    final = (day.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
    return day.weekday() == 4 and final - day < timedelta(days=7)

def is_premiumer_friday(day):
    return is_premium_friday(day) and day.month % 3 == 0

def is_premiumest_friday(day):
    return is_premium_friday(day) and day.month == 12

def is_all_premiums(day):
    return all(func(day) for func in [is_premium_friday, is_premiumer_friday, is_premiumest_friday])

today = datetime.today()
input_date = input("Enter a date (YYYY-MM-DD), or press Enter to use today's date: ")

if input_date == '':
    day = today
else:
    day = datetime.strptime(input_date, "%Y-%m-%d")

if is_all_premiums(day):
    print("This date is Premium, Premiumer, and Premiumest Friday")
elif is_premium_friday(day) and is_premiumer_friday(day):
    print("This date is both Premium and Premiumer Friday")
elif is_premium_friday(day) and is_premiumest_friday(day):
    print("This date is both Premium and Premiumest Friday")
elif is_premiumer_friday(day) and is_premiumest_friday(day):
    print("This date is both Premiumer and Premiumest Friday")
elif is_premium_friday(day):
    print("This date is Premium Friday")
else:
    print("This date is not a Premium Friday")
