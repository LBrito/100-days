import datetime


def add_gigasecond(moment):
    return moment + datetime.timedelta(0, 10 ** 9)
