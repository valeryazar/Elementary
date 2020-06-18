# 19 Task. Date and Time Converter
from datetime import datetime


def date_time(time: str) -> str:
    date = datetime.strptime(time, '%d.%m.%Y %H:%M')
    hour = 'hour' if date.hour == 1 else 'hours'
    minute = 'minute' if date.minute == 1 else 'minutes'
    return date.strftime('{} %B %Y year {} {} {} {}').format(date.day, date.hour, hour, date.minute, minute)


if __name__ == '__main__':
    print("Result =", date_time('01.01.2000 00:00'))