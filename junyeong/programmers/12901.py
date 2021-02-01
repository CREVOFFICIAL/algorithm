import datetime

def solution(a, b):
    date = datetime.datetime(2016, a, b)
    day = date.strftime("%a")
    return day.upper()
