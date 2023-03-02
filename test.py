import datetime


def get_stock_date(today, target_weekday):
    days_until_target = (target_weekday - today.weekday()) % 7
    next_target_date = today + datetime.timedelta(days=days_until_target)

    if next_target_date.month != (next_target_date + datetime.timedelta(days=7)).month:
        stock_date = next_target_date.strftime("%y%b").upper()
    else:
        stock_date = next_target_date.strftime("%y%m%d")

    return stock_date

#loop from today to next 40 days and print date, day, stockdate in loop
today = datetime.date.today()
target_weekday = 3

for i in range(40):
    current_date = today + datetime.timedelta(days=i)
    current_day = current_date.strftime("%A")
    current_stock_date = get_stock_date(current_date, target_weekday)
    print(f"{current_date} ({current_day}): {current_stock_date}")
