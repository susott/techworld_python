
# EXERCISE 8: Working with Dates

# Write a program that:

# accepts user's birthday as input
# and calculates how many days, hours and minutes are remaining till the birthday
# prints out the result as a message to the user

from datetime import datetime

user_input = input('Please enter your birthday. Example format: 01.05.\n')
today = datetime.now()

try:
    day_part, month_part, year_part = user_input.split('.')
    day = int(day_part.strip())
    month = int(month_part.strip())
    birthday_this_year = datetime(today.year, month, day)
except (TypeError, ValueError, NameError):
    print('Please enter a date. E.g. 1.5.')

if birthday_this_year > today:
    time_difference = birthday_this_year - today
    hours_remaining = time_difference.seconds / 60 / 60  # TODO: hours and minutes

    print(f"{time_difference.days} days and {round(hours_remaining)} hours till your next birthday")
elif birthday_this_year == today:  # ?
    print("Congratulations. Your birthday is today!")
else:
    birthday_next_year = birthday_this_year.replace(year=today.year + 1)
    print(birthday_next_year - today)
