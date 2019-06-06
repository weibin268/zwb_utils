import datetime
import time

DEFUALT_DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'


def to_string(date: datetime.datetime):
    return date.strftime(DEFUALT_DATETIME_FORMAT)


def to_datetime(str):
    return datetime.datetime.strptime(str, DEFUALT_DATETIME_FORMAT)


if __name__ == "__main__":
    print(to_string(datetime.datetime.now()))
    print(to_datetime("2019-01-01 00:00:00"))
