# Aggregation in Pandas
import pandas as pd
import numpy as np


def filter_func(x):
    return x['data2'].std() > 4


def norm_by_data2(x):
    # x is a DataFrame of group values
    x['data1'] /= x['data2'].sum()
    return x


def before_combining():
    rng = np.random.RandomState(0)
    df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                       'data1': range(6),
                       'data2': rng.randint(0, 10, 6)},
                      columns=['key', 'data1', 'data2'])
    print('df \r\n', df)
    # take a string, a function, or a list thereof, and compute all the aggregates at once
    agg1 = df.groupby('key').aggregate(['min', np.median, max])
    print(agg1)
    agg2 = df.groupby('key').aggregate({'data1': 'min',
                                        'data2': 'max'})
    print(agg2)
    agg3 = df.groupby('key').std()
    print(agg3)
    filt = df.groupby('key').filter(filter_func) # drop data based on the group properties.
    print(filt)
    t = df.groupby('key').transform(lambda x: x - x.mean()) # some transformed version of the full data to recombine.
    print(t)
    # apply an arbitrary function to the group results
    a = df.groupby('key').apply(norm_by_data2)
    print(a)

    # Specifying the split key
    L = [0, 1, 0, 1, 2, 0]
    s1= df.groupby(L).sum() # A list, array, series, or index providing the grouping keys
    print(s1)
    s2 = df.groupby(df['key']).sum()
    print(s2)
    df2 = df.set_index('key')
    mapping = {'A': 'vowel', 'B': 'consonant', 'C': 'consonant'}
    s3 = df2.groupby(mapping).sum() # dictionary
    print(s3)
    agg4 = df2.groupby(str.lower).mean() # function
    print(agg4)
    agg5 = df2.groupby([str.lower, mapping]).mean() # list
    print(agg5)


def simple_agg():
    rng = np.random.RandomState(42)
    ser = pd.Series(rng.rand(5))
    print('Series:\r\n', ser)
    print('sum: ', ser.sum())
    print('mean: ', ser.mean())
    df = pd.DataFrame({'A': rng.rand(5),
                       'B': rng.rand(5)})
    print('DataFrame:\r\n', df)
    print('mean\r\n: ', df.mean())
    print('mean(axis="columns"):\r\n ', df.mean(axis='columns'))
    df2 = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'],
                       'data': range(6)}, columns=['key', 'data'])
    print('DataFrame:\r\n', df2)
    print('groupby("key").sum():\r\n', df2.groupby('key').sum())


if __name__ == '__main__':
    print('Numpy Version:', np.__version__)
    print('Pandas Version:', pd.__version__)
    simple_agg()
    before_combining()
