from datetime import date, timedelta

def is_premium_friday(day):
    final = (day.replace(day=28) + timedelta(days=4)).replace(day=1) - timedelta(days=1)
    return day.weekday() == 4 and final - day < timedelta(days=7)

def is_premiumer_friday(day):
    return is_premium_friday(day) and day.month % 3 == 0

def is_premiumest_friday(day):
    return is_premium_friday(day) and day.month == 12

def is_all_premiums(day):
    if is_premiumest_friday(day):
        return "This date is Premium, Premiumer, and Premiumest Friday"
    elif is_premiumer_friday(day):
        return "This date is Premiumer and Premium Friday"
    elif is_premium_friday(day):
        return "This date is Premium Friday"
    else:
        return "This date is not a Premium Friday"

def get_user_input():
    user_input = input("Hit return to check Today or enter a date in this format(YYYY-MM-DD): ")
    if not user_input:
        today = date.today()
        return today
    else:
        year, month, day = user_input.split("-")
        return date(int(year), int(month), int(day))

day = get_user_input()
print(is_all_premiums(day))

