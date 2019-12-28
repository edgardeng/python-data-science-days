# Pandas Data Selection

import pandas as pd
import numpy as np
import timeit


def series_selection():
    data = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
    print('b in data:', 'b' in data)
    print('data.keys:', data.keys())
    print('list(data.items()):', list(data.items()))
    data['e'] = 1.25
    print('data: ', data)
    print('data[a:c]:', data['a':'c'])  # slicing by explicit index
    print('data[1:3]:', data[1:3])  # slicing by implicit integer index
    print('data[ data>0.3 & data<0.8]:', data[(data > 0.3) & (data < 0.8)])  # masking
    print('data[a, e]:', data[['a', 'e']])  # fancy indexing

    data = pd.Series(['a', 'b', 'c'], index=[1, 3, 5])
    print('data.loc[1]', data.loc[1])
    print('data.loc[1:3]', data.loc[1:3])
    print('data.iloc[1]', data.loc[1])
    print('data.iloc[1:3]', data.loc[1:3])


def data_frame_selection():
    area = pd.Series({'California': 423967, 'Texas': 695662,
                      'New York': 141297, 'Florida': 170312,
                      'Illinois': 149995})
    pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                     'New York': 19651127, 'Florida': 19552860,
                     'Illinois': 12882135})
    data = pd.DataFrame({'area':area, 'pop':pop})
    print('data.area is data[\'area\']', data.area is data['area'])
    print('data.pop is data[\'pop\']', data.pop is data['pop']) # the ``DataFrame`` has a ``pop()`` method
    data['density'] = data['pop'] / data['area']
    print('data: \r\n', data)

    # examine the raw underlying data array using the values attribute:
    print('data.values: \r\n', data.values)
    # swap rows and columns:
    print('data.T: \r\n', data.T)
    #  passing a single index to an array accesses a row:
    print('data.values[0]: \r\n', data.values[0])
    # passing a single "index" to a DataFrame accesses a column:
    print('data[area]: \r\n', data['area'])

    print('data.iloc[:3, :2]:\r\n', data.iloc[:3, :2])
    print('data.iloc[:Illinois, :pop]:\r\n', data.loc[:'Illinois', :'pop'])
    # ix -- a hybrid of these two approaches
    print('data.data.ix[:3, :\'pop\']:\r\n', data.ix[:3, :'pop'])
    # combine masking and fancy indexing
    print('data.loc[data.density > 100, [\'pop\', \'density\']]:\r\n')
    print(data.loc[data.x > 100, ['pop', 'density']])
    data.iloc[0, 2] = 90
    print('after data.iloc[0, 2] = 90:\r\n')
    print(data)


def ufunc_index():
    rng = np.random.RandomState(42)
    ser = pd.Series(rng.randint(0, 10, 4))
    arr = rng.randint(0, 10, (3, 4))
    print(arr)
    df = pd.DataFrame(arr, columns=['A', 'B', 'C', 'D'])
    print('Series:\r\n', ser)
    print('np.exp(ser):\r\n', np.exp(ser))
    print('DataFrame:\r\n', df)
    print('np.sin(df * np.pi / 4):\r\n', np.sin(df * np.pi / 4))

    area = pd.Series({'Alaska': 1723337, 'Texas': 695662,
                      'California': 423967}, name='area')
    pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                     'New York': 19651127}, name='population')
    print('population / area : \r\n', pop / area)
    print('area.index | population.index:', area.index | pop.index)

    a = pd.Series([2, 4, 6], index=[0, 1, 2])
    b = pd.Series([1, 3, 5], index=[1, 2, 3])
    print('A + B: \r\n', a + b)
    print('A.add(B, fill_value=0): \r\n', a.add(b, fill_value=0))

    c = pd.DataFrame(rng.randint(0, 20, (2, 2)), columns=list('AB'))
    d = pd.DataFrame(rng.randint(0, 10, (3, 3)), columns=list('BAC'))
    print('c: \r\n', c)
    print('d: \r\n', d)
    print('c + d: \r\n', c + d)
    fill = c.stack().mean()
    print('fill: ', fill)
    print('c.add(d, fill_value=fill): \r\n', c.add(d, fill_value=fill))

    data = rng.randint(10, size=(3, 4))
    print('data:\r\n', data)
    print('data - data[0]:\r\n', data - data[0])
    df_2 = pd.DataFrame(data, columns=list('ABCD'))
    print('df - df.iloc[0]:\r\n', df_2 - df_2.iloc[0])  # operates row-wise
    print('df_2.subtract(df_2[\'A\'], axis=0) \r\n', df_2.subtract(df_2['A'], axis=0)) # operate column-wise
    half_row = df_2.iloc[0, ::2]
    print('df_2.iloc[0, ::2] \r\n', half_row)
    print('df_2 - df_2.iloc[0, ::2] ', df_2 - half_row)


def sum_object():
    print(np.arange(1E6, dtype='object').sum())


def sum_int():
    print(np.arange(1E6, dtype='int').sum())


def missing_data():
    val = np.array([1, None, 3, 4])
    print("dtype = object")
    timeit.timeit(sum_object, number=1)
    print("dtype = int")
    timeit.timeit(sum_int, number=1)
    # print('val.sum', val.sum()) # TypeError unsupported operand type(s) for +: 'int' and 'NoneType'

    val_2 = np.array([1, np.nan, 3, 4])
    print('val_e.dtype:', val_2.dtype)
    print('1 + np.nan:', 1 + np.nan)
    print('0 *  np.nan:', 0 * np.nan)
    print(np.nansum(val_2), np.nanmin(val_2), np.nanmax(val_2)) # 8, 1, 4
    print(val_2.sum(), val_2.min(), val_2.max())  # nan, nan, nan

    series = pd.Series([1, np.nan, 2, None])
    print('series \r\n', series)
    series[0] = None
    print('series \r\n', series)
    print('series.isnull() :', series.isnull())
    print('series[data.notnull()] \r\n', series[series.notnull()])
    print('series.dropna() \r\n', series.dropna())
    print('series.fillna(0) \r\n', series.fillna(0))

    df = pd.DataFrame([[1,      np.nan, 2],
                       [2,      3,      5],
                       [np.nan, 4,      6]])
    print('df.dropna() \r\n', df.dropna())
    print('df.dropna(axis=columns) \r\n', df.dropna(axis='columns'))  # axis = 1
    df[3] = np.nan
    print('df \r\n', df)
    print('dropna(axis=columns, how=all) \r\n', df.dropna(axis='columns', how='all'))
    print('dropna(axis=rows, thresh=3) \r\n', df.dropna(axis='rows', thresh=3))
    print('fillna(0)\r\n', df.fillna(0))
    print('fillna(ffill)\r\n', df.fillna(method='ffill'))
    print('fillna(bfill)\r\n', df.fillna(method='bfill'))
    print('fillna(method=\'ffill\', axis=1)\r\n', df.fillna(method='ffill', axis=1))


def hierarchical_index():
    index = [('California', 2000), ('California', 2010),
             ('New York', 2000), ('New York', 2010),
             ('Texas', 2000), ('Texas', 2010)]
    pop = [33871648, 37253956,
           18976457, 19378102,
           20851820, 25145561]
    # a bad way
    series = pd.Series(pop, index=index)
    print('series: \r\n', series)
    series[('California', 2010):('Texas', 2000)]
    series[[i for i in series.index if i[1] == 2010]] # select all values from 2010,

    # a good way
    index_2 = pd.MultiIndex.from_tuples(index)
    print('index_2: ', index_2)
    series_pop = series.reindex(index_2)
    print('series_pop: \r\n', series_pop)
    print('series_pop[:, 2010]: \r\n', series_pop[:, 2010]) # access all data for which the second index is 2010

    #  quickly convert a multiply indexed ``Series`` into a conventionally indexed ``DataFrame``:
    df = series_pop.unstack()
    print('unstack \r\n', df)
    print(series_pop.unstack(level=0))
    print(series_pop.unstack(level=1))
    print('unstack & stack \r\n', series_pop.unstack().stack())

    pop_df = pd.DataFrame({'total': series_pop,
                           'under18': [9267089, 9284094,
                                       4687374, 4318033,
                                       5906301, 6879014]})
    print('pop_df: \r\n', pop_df)
    f_u18 = pop_df['under18'] / pop_df['total']
    print('pop_df[\'under18\'] / pop_df[\'total\'] \r\n', f_u18)
    print('f_u18.unstack() \r\n', f_u18.unstack())
    series_pop.index.names = ['state', 'year']
    print(series_pop)

    index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]], names=['year', 'visit'])
    print('index', index)
    columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']], names=['subject', 'type'])
    print('columns', columns)
    data = np.round(np.random.randn(4, 6), 1) # mock some data
    data[:, ::2] *= 10
    data += 37
    print(data)
    # create the DataFrame
    health_data = pd.DataFrame(data, index=index, columns=columns)
    print(health_data)
    print(health_data['Guido'])

    print(series_pop['California', 2000])  #  indexing with multiple terms:
    print(series_pop.loc['California':'New York']) # partial indexing
    print(series_pop[:, 2000])
    print(series_pop[series_pop > 22000000]) #  Boolean masks:
    print(series_pop[['California', 'Texas']]) # fancy indexing

    print(health_data['Guido', 'HR']) # index
    # ``loc``, ``iloc``, and ``ix`` indexers
    print(health_data.iloc[:2, :2])
    print(health_data.loc[:, ('Bob', 'HR')])
    # print(health_data.loc[(:, 1), (:, 'HR')]) # these index tuples is not especially convenient;
    idx = pd.IndexSlice
    print(health_data.loc[idx[:, 1], idx[:, 'HR']])

    print('mean:level=year \r\n', health_data.mean(level='year'))
    print('mean:axis=1, level=\'type\'\r\n', health_data.mean(axis=1, level='type'))

    pop_flat = series_pop.reset_index(name='population')
    print(pop_flat)
    print(pop_flat.set_index(['state', 'year']))


def rearranging_multi_index():
    index = pd.MultiIndex.from_product([['a', 'c', 'b'], [1, 2]])
    data = pd.Series(np.random.rand(6), index=index)
    data.index.names = ['char', 'int']
    print(data)
    try:
        data['a':'b']
    except KeyError as e:
        print(type(e))
        print(e)
    data = data.sort_index()
    print(data)
    print('data[\'a\':\'b\'] \r\n', data['a':'b'])


if __name__ == '__main__':
    print('Numpy Version:', np.__version__)
    print('Pandas Version:', pd.__version__)
    # series_selection()
    # data_frame_selection()
    ufunc_index()
    # missing_data()
    # hierarchical_index()
    # rearranging_multi_index()
