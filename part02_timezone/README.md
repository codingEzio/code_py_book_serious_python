### Basic concepts

- _UTC_ versus _GMT_ <small>(see [more](https://www.timeanddate.com/time/gmt-utc-time.html))</small>

  1. [_UTC_](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) is a **standard**.
  2. [_GMT_](https://en.wikipedia.org/wiki/Greenwich_Mean_Time) is a _time-zone_, just like [_PDT_](https://en.wikipedia.org/wiki/Pacific_Time_Zone#Daylight_time) or [else](https://en.wikipedia.org/wiki/List_of_time_zone_abbreviations).

- Why it's _hard_ to get this right
  - Cases you might need to consider
    - timestamps _without time zones attached_
    - time zone with _15 minute granularity_
    - countries that _change time zones twice a year_
    - countries that use a _custom time zone during summer_, aka. _daylight saving time_
  - Possible solutions
    1. **raise an error** if no time zone is provided
    2. make clear **what time zone is assumed**, for example, _UTC_

### More on this

- Go see the _code_.
