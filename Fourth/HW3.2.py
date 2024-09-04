import datetime

string_datetime = input()


def parse_time(s):
    d_parse = datetime.datetime.strptime(s, '%Y %m %d %H %M %S')
    delta = datetime.timedelta(days=1)
    return (d_parse + delta).day


print(parse_time(string_datetime))
