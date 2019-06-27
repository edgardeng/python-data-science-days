## Time Series in Pandas

Pandas contains a fairly extensive set of tools for working with dates, times, and time-indexed data

* Time stamps reference particular moments in time (e.g., July 4th, 2015 at 7:00am).
* Time intervals and periods reference a length of time between a particular beginning and end point; for example, the year 2015. Periods usually reference a special case of time intervals in which each interval is of uniform length and does not overlap (e.g., 24 hour-long periods comprising days).
* Time deltas or durations reference an exact length of time (e.g., a duration of 22.56 seconds).


### Native Python dates and times

```python 
from datetime import datetime
date1 = datetime(year=2015, month=7, day=4)

from dateutil import parser
date2  = parser.parse("4th of July, 2015")
date2.strftime('%A')
```

### Typed arrays of times: NumPy's ``datetime64``

The weaknesses of Python's datetime format inspired the NumPy team to add a set of native time series data type to NumPy.
The ``datetime64`` dtype encodes dates as 64-bit integers, and thus allows arrays of dates to be represented very compactly.

|Code    | Meaning     | Time span (relative) | Time span (absolute)   |
|--------|-------------|----------------------|------------------------|
| ``Y``  | Year	       | ± 9.2e18 years       | [9.2e18 BC, 9.2e18 AD] |
| ``M``  | Month       | ± 7.6e17 years       | [7.6e17 BC, 7.6e17 AD] |
| ``W``  | Week	       | ± 1.7e17 years       | [1.7e17 BC, 1.7e17 AD] |
| ``D``  | Day         | ± 2.5e16 years       | [2.5e16 BC, 2.5e16 AD] |
| ``h``  | Hour        | ± 1.0e15 years       | [1.0e15 BC, 1.0e15 AD] |
| ``m``  | Minute      | ± 1.7e13 years       | [1.7e13 BC, 1.7e13 AD] |
| ``s``  | Second      | ± 2.9e12 years       | [ 2.9e9 BC, 2.9e9 AD]  |
| ``ms`` | Millisecond | ± 2.9e9 years        | [ 2.9e6 BC, 2.9e6 AD]  |
| ``us`` | Microsecond | ± 2.9e6 years        | [290301 BC, 294241 AD] |
| ``ns`` | Nanosecond  | ± 292 years          | [ 1678 AD, 2262 AD]    |
| ``ps`` | Picosecond  | ± 106 days           | [ 1969 AD, 1970 AD]    |
| ``fs`` | Femtosecond | ± 2.6 hours          | [ 1969 AD, 1970 AD]    |
| ``as`` | Attosecond  | ± 9.2 seconds        | [ 1969 AD, 1970 AD]    |

Dates and times in pandas

```python

import pandas as pd
date = pd.to_datetime("4th of July, 2015")
date.strftime('%A')
date + pd.to_timedelta(np.arange(12), 'D')
```

### Pandas Time Series

#### Indexing by Time

```python
    index = pd.DatetimeIndex(['2014-07-04', '2014-08-04',
                              '2015-07-04', '2015-08-04'])
    data = pd.Series([0, 1, 2, 3], index=index)
    data['2014-07-04':'2015-07-04']
    print(data['2015'])
```

#### Pandas Time Series Data Structures

```python
    dates = pd.to_datetime(
        [datetime(2015, 7, 3), '4th of July, 2015', '2015-Jul-6', '07-07-2015', '20150708'])
    print(dates.to_period('D'))
    print(dates - dates[0])
```

#### Regular sequences `pd.date_range()`

```python
    date_range1 = pd.date_range('2015-07-03', '2015-07-10')
    date_range2 = pd.date_range('2015-07-03', periods=8)  # 2015-07-03', '2015-07-04'
    date_range3 = pd.date_range('2015-07-03', periods=8, freq='H')  # 015-07-03 00:00:00
    date_range4 = pd.period_range('2015-07', periods=8, freq='M')  # 2015-07', '2015-08'
    date_range5 = pd.period_range('2015-07', periods=8, freq='M')
    print(pd.date_range('12:12:12', periods=8)) # start from today(2019-06-27 12:12:12) with 8 days
    date_range7 = pd.timedelta_range(0, periods=10, freq='H') # '00:00:00'
    
```

codes to specify any desired frequency spacing:


| Code   | Description         | Code   | Description          |
|--------|---------------------|--------|----------------------|
| ``D``  | Calendar day        | ``B``  | Business day         |
| ``W``  | Weekly              |        |                      |
| ``M``  | Month end           | ``BM`` | Business month end   |
| ``Q``  | Quarter end         | ``BQ`` | Business quarter end |
| ``A``  | Year end            | ``BA`` | Business year end    |
| ``H``  | Hours               | ``BH`` | Business hours       |
| ``T``  | Minutes             |        |                      |
| ``S``  | Seconds             |        |                      |
| ``L``  | Milliseonds         |        |                      |
| ``U``  | Microseconds        |        |                      |
| ``N``  | nanoseconds         |        |                      |

The monthly, quarterly, and annual frequencies are all marked at the end of the specified period. By adding an S suffix to any of these, they instead will be marked at the beginning:

| Code    | Description            || Code    | Description            |
|---------|------------------------||---------|------------------------|
| ``MS``  | Month start            ||``BMS``  | Business month start   |
| ``QS``  | Quarter start          ||``BQS``  | Business quarter start |
| ``AS``  | Year start             ||``BAS``  | Business year start    |

Additionally, you can change the month used to mark any quarterly or annual code by adding a three-letter month code as a suffix:

Q-JAN, BQ-FEB, QS-MAR, BQS-APR, etc.
A-JAN, BA-FEB, AS-MAR, BAS-APR, etc.
In the same way, the split-point of the weekly frequency can be modified by adding a three-letter weekday code:

W-SUN, W-MON, W-TUE, W-WED, etc.

[DateOffset](http://pandas.pydata.org/pandas-docs/stable/timeseries.html#dateoffset-objects) section of the Pandas documentation.

#### Resampling, Shifting, and Windowing
