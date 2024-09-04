import datetime

days, seconds = int(input()), int(input())


def shift_time(days: int, seconds: int):
    time = datetime.datetime(2023, 1, 1, 12, 30, 00)
    delta = datetime.timedelta(days, seconds)
    time = time + delta
    return (time.day, time.second)


print(shift_time(days, seconds))
