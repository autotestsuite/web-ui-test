import datetime

DATETIME_FULL = '%Y-%m-%d %H:%M:%S'

DATETIME_SHORT = '%Y-%m-%d %H:%M'

DATETIME_DATE = '%Y-%m-%d'

DATETIME_TIME = '%H:%M:%S'

UTC_DATETIME = '%Y-%m-%dT%H:%M:%S.000Z'


def get_timestamp() -> int:
    return int(datetime.datetime.timestamp(datetime.datetime.now()))


def get_utc_datetime() -> datetime.datetime:
    return datetime.datetime.utcnow()


def format_datetime(dt: datetime.datetime, time_format: str) -> str:
    return dt.strftime(time_format)


def get_current_date():
    return datetime.datetime.now().date().isoformat()


def get_current_time():
    return datetime.datetime.now().strftime(DATETIME_FULL)


def add_days(date_str, days):
    date = datetime.datetime.fromisoformat(date_str)
    new_date = date + datetime.timedelta(days=days)
    return new_date.date().isoformat()


def add_hours_and_days(datetime_str, hours, days):
    dt = datetime.datetime.strptime(datetime_str, DATETIME_FULL)
    new_dt = dt + datetime.timedelta(hours=hours, days=days)
    return new_dt.strftime(DATETIME_FULL)
