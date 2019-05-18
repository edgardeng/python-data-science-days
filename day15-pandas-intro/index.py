# Introduction to Pandas

import pandas as pd
import numpy as np


def series_data():
    data = pd.Series([0.25, 0.5, 0.75, 1.0])
    print('data:', data)
    print('data.values:', data.values)
    print('data.index:', data.index)
    print('data[1]:', data[1])
    print('data[:2]:', data[:2])


def series_as():
    data_1 = pd.Series([0.25, 0.5, 0.75, 1.0], index=['a', 'b', 'c', 'd'])
    print('data[\'a\'] = ', data_1['a'])
    data_2 = pd.Series([0.25, 0.5, 0.75, 1.0], index=[3, 5, 6, 4])
    print('data[5] = ', data_2[5])
    dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    data_3 = pd.Series(dict)
    print('data[\'a\'] = ', data_3['a'])
    print('data[\'a\':\'c\'] = ', data_3['a': 'c'])


def data_frame_as():
    population = {'California': 38332521,
                  'Texas': 26448193,
                  'New York': 19651127,
                  'Florida': 19552860,
                  'Illinois': 12882135}
    area = {'California': 423967,
            'Texas': 695662,
            'New York': 141297,
            'Florida': 170312,
            'Illinois': 149995}
    data = pd.DataFrame({'population': population, 'area': area})
    print('data: ', data)
    print('data.index: ', data.index)
    print('data.columns:', data.columns)
    print('data[\'area\']:', data['area'])


def index_object():
    ind = pd.Index([2, 3, 5, 7, 11])
    print('index: ', ind)
    print('index[1]: ', ind[1])
    print('index[::2]: ', ind[::2])
    print('index.size:', ind.size)
    print('index.shape:', ind.shape)
    print('index.ndim:', ind.ndim)
    print('index.dtype:', ind.dtype)
    # ind[1] = 0 # TypeError: cannot be modified

    ind_2 = pd.Index([1, 3, 5, 7, 9])
    print('index2: ', ind_2)
    print(' & : ', ind & ind_2)  # intersection
    print(' | : ', ind | ind_2)  # union
    print(' ^ ', ind ^ ind_2)  # symmetric difference


if __name__ == '__main__':
    print('Numpy Version:', np.__version__)
    print('Pandas Version:', pd.__version__)
    # series_data()
    # series_as()
    data_frame_as()
    # index_object()
