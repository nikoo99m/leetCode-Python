import datetime


def find_day(day, month, year):

    date = datetime.date(year, month, day)

    return date.strftime("%A")


# Example usage
day = 8
month = 9
year = 2024
print(find_day(day, month, year))
