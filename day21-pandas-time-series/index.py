# Pandas Time Series

import pandas as pd
import numpy as np
from datetime import datetime
from dateutil import parser
from pandas_datareader import data

import matplotlib.pyplot as plt


def simple_example():
    # datetime in python
    datetime_1 = datetime(year=2015, month=7, day=4)
    print(datetime_1)
    date = parser.parse("4th of July, 2015")
    print(date.strftime('%A'))
    date_2 = np.array('2015-07-04', dtype=np.datetime64)
    print(date_2)
    print(date_2 + np.arange(12))
    np.datetime64('2015-07-04')
    np.datetime64('2015-07-04 12:00')
    print(np.datetime64('2015-07-04 12:59:59.50', 'ns'))


def time_series():
    index = pd.DatetimeIndex(['2014-07-04', '2014-08-04',
                              '2015-07-04', '2015-08-04'])
    data = pd.Series([0, 1, 2, 3], index=index)
    data['2014-07-04':'2015-07-04']
    print(data['2015'])

    dates = pd.to_datetime(
        [datetime(2015, 7, 3), '4th of July, 2015', '2015-Jul-6', '07-07-2015', '20150708'])
    print(dates)
    print(dates.to_period('D'))
    print(dates - dates[0])
    date_range1 = pd.date_range('2015-07-03', '2015-07-10')
    date_range2 = pd.date_range('2015-07-03', periods=8)  # 2015-07-03', '2015-07-04'
    date_range3 = pd.date_range('2015-07-03', periods=8, freq='H')  # 015-07-03 00:00:00
    date_range4 = pd.period_range('2015-07', periods=8, freq='M')  # 2015-07', '2015-08'
    date_range5 = pd.period_range('2015-07', periods=8, freq='M')
    print(pd.date_range('12:12:12', periods=8)) # start from today(2019-06-27 12:12:12) with 8 days
    date_range7 = pd.timedelta_range(0, periods=10, freq='H') # '00:00:00'
    print(date_range7)
    pd.timedelta_range(0, periods=9, freq="2H30T")
    pd.date_range('2015-07-01', periods=5, freq=BDay())


def data_stack():
    goog = data.DataReader('GOOG', start='2004', end='2016',
                           data_source='google')
    goog.head()
    goog = goog['Close']
    goog.plot()

    goog.plot(alpha=0.5, style='-')
    goog.resample('BA').mean().plot(style=':')
    goog.asfreq('BA').plot(style='--');
    plt.legend(['input', 'resample', 'asfreq'], loc='upper left')

    fig, ax = plt.subplots(2, sharex=True)
    data = goog.iloc[:10]
    data.asfreq('D').plot(ax=ax[0], marker='o')
    data.asfreq('D', method='bfill').plot(ax=ax[1], style='-o')
    data.asfreq('D', method='ffill').plot(ax=ax[1], style='--o')
    ax[1].legend(["back-fill", "forward-fill"]);

    ## Time-shifts
    fig, ax = plt.subplots(3, sharey=True)
    # apply a frequency to the data
    goog = goog.asfreq('D', method='pad')

    goog.plot(ax=ax[0])
    goog.shift(900).plot(ax=ax[1])
    goog.tshift(900).plot(ax=ax[2])

    # legends and annotations
    local_max = pd.to_datetime('2007-11-05')
    offset = pd.Timedelta(900, 'D')

    ax[0].legend(['input'], loc=2)
    ax[0].get_xticklabels()[2].set(weight='heavy', color='red')
    ax[0].axvline(local_max, alpha=0.3, color='red')
    ax[1].legend(['shift(900)'], loc=2)
    ax[1].get_xticklabels()[2].set(weight='heavy', color='red')
    ax[1].axvline(local_max + offset, alpha=0.3, color='red')

    ax[2].legend(['tshift(900)'], loc=2)
    ax[2].get_xticklabels()[1].set(weight='heavy', color='red')
    ax[2].axvline(local_max + offset, alpha=0.3, color='red');
    ROI = 100 * (goog.tshift(-365) / goog - 1)
    ROI.plot()
    plt.ylabel('% Return on Investment');
    # Rolling windows

    rolling = goog.rolling(365, center=True)
    data = pd.DataFrame({'input': goog,
                         'one-year rolling_mean': rolling.mean(),
                         'one-year rolling_std': rolling.std()})
    ax = data.plot(style=['-', '--', ':'])
    ax.lines[0].set_alpha(0.3)


if __name__ == '__main__':
    print('Numpy Version:', np.__version__)
    print('Pandas Version:', pd.__version__)
    # simple_example()
    time_series()