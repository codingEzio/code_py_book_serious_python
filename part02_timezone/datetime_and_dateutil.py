from datetime import datetime

from dateutil import tz
from dateutil.zoneinfo import get_zonefile_instance
import iso8601


UTCNOW = datetime.utcnow()
UTCNOW_TZ = datetime.now(tz=tz.tzutc())  # plus '+HH:MM'

# either based on country or offset
# see more at https://en.wikipedia.org/wiki/Lists_of_time_zones
TZ_GMT8 = tz.gettz("GMT+8")
TZ_PARIS = tz.gettz("Europe/Paris")
TZ_HONGKONG = tz.gettz("Hongkong")


def how_many_timezone_are_there() -> None:
    zones = list(get_zonefile_instance().zones)
    assert len(zones) == 595


def assign_timezone_to_a_time() -> None:
    assert UTCNOW.tzinfo is None

    # `replace` return a new time with new vals for the specified fields
    print("GMT8     :", UTCNOW.replace(tzinfo=TZ_GMT8))
    print("Hongkong :", UTCNOW.replace(tzinfo=TZ_HONGKONG))


def determine_timezone_by_yourself(time_example=UTCNOW) -> str:
    localzone = tz.gettz()
    return localzone.tzname(time_example)


def serializing_datetime_ojbect() -> None:
    # time | time-isoformat-string
    UTCNOW_TZ
    UTCNOW_TZ.isoformat()

    # datetime -> string -> datetime(instead of str)
    assert UTCNOW_TZ == iso8601.parse_date(UTCNOW_TZ.isoformat())


def ambiguous_date_cuz_of_DST() -> None:
    # possible ambiguous datetime cuz of DST
    # 2nd half of 2019: https://www.timeanddate.com/time/dst/2019.html
    paris_amb_date = datetime(2017, 10, 29, 2, 30, tzinfo=TZ_PARIS)
    assert TZ_PARIS.is_ambiguous(datetime(2017, 10, 29, 2, 30)) is True

    # for dates might be ambiguous, you might need `fold` attr
    # https://www.python.org/dev/peps/pep-0495/#the-fold-attribute
    print(paris_amb_date.replace(fold=0))
    print(paris_amb_date.replace(fold=1))
