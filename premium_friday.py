from datetime import date, timedelta

def is_premium_friday(day):
    final = (day.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
    return day.weekday() == 4 and final - day < timedelta(days=7)

def is_premiumer_friday(day):
    return is_premium_friday(day) and day.month % 3 == 0

def is_premiumest_friday(day):
    return is_premium_friday(day) and day.month == 12

today = date.today()
print(f"Today ({today}) is Premium Friday? {is_premium_friday(today)}")
print(f"March 31, 2023 is Premium Friday? {is_premium_friday(date(2023, 3, 31))}")
print(f"March 31, 2023 is Premiumer Friday? {is_premiumer_friday(date(2023, 3, 31))}")
print(f"December 29, 2023 is Premium Friday? {is_premium_friday(date(2023, 12, 29))}")
print(f"December 29, 2023 is Premiumest Friday? {is_premiumest_friday(date(2023, 12, 29))}")
