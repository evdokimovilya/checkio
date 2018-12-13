# https://py.checkio.org/en/mission/days-diff/

from datetime import date, timedelta


def days_diff(date1, date2):
    date_2 = date(date2[0], date2[1], date2[2])
    date_1 = date(date1[0], date1[1], date1[2])
    a = abs((date_2 - date_1).days)
    return a
