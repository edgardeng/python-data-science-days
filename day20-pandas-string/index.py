# Pandas String Operate

import pandas as pd
import numpy as np


def simple_example():
    data = ['peter', 'Paul', None, 'MARY', 'gUIDO']
    try:
        data_2 = [s.capitalize() for s in data]
    except TypeError as e:
        print(e)
    names = pd.Series(data)
    print(names.str.capitalize())


def regular_expressions():
    monte = pd.Series(['Graham Chapman', 'John Cleese', 'Terry Gilliam',
                       'Eric Idle', 'Terry Jones', 'Michael Palin'])
    monte.str.extract('([A-Za-z]+)', expand=False) # extract the first name
    monte.str.findall(r'^[^AEIOU].*[^aeiou]$') #  start and end with a consonant
    monte.str[0:3]
    monte.str.split().str.get(-1)
    full_monte = pd.DataFrame({'name': monte,
                               'info': ['B|C|D', 'B|D', 'A|C', 'B|D', 'B|C', 'B|C|D']})

    full_monte['info'].str.get_dummies('|') #  split-out these indicator variables into a DataFrame



if __name__ == '__main__':
    print('Numpy Version:', np.__version__)
    print('Pandas Version:', pd.__version__)
    simple_example()
