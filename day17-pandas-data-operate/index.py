# Pandas Data Operation

import pandas as pd
import numpy as np


def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)


def concatenation():
    x = [1, 2, 3]
    y = [4, 5, 6]
    z = [7, 8, 9]
    print('np.concatenate([x, y, z]) \r\n', np.concatenate([x, y, z]))
    x = [[1, 2],
         [3, 4]]
    print('np.concatenate([x, x], axis=1) \r\n', np.concatenate([x, x], axis=1))

    ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
    ser2 = pd.Series(['D', 'E', 'F'], index=[3, 5, 6])
    print(pd.concat([ser1, ser2]))

    df1 = make_df('AB', [1, 2])
    df2 = make_df('AB', [3, 4])
    print('df1 \r\n', df1)
    print('df2 \r\n', df2)
    print(pd.concat([df1, df2]))

    df3 = make_df('AB', [0, 1])
    df4 = make_df('CD', [0, 1])
    print('df3 \r\n', df3)
    print('df4 \r\n', df4)
    print(pd.concat([df3, df4], axis=1))  # can't use the intuitive axis='col'.

    # Duplicate indices
    x = make_df('AB', [0, 1])
    y = make_df('AB', [2, 3])
    y.index = x.index  # make duplicate indices!
    print('x \r\n', x)
    print('y \r\n', y)
    print('Duplicate indices \r\n', pd.concat([x, y]))
    # Catching the repeats as an error¶
    try:
        pd.concat([x, y], verify_integrity=True)
    except ValueError as e:
        print("ValueError:", e)
    # Ignoring the index
    print('ignore_index=sTrue \r\n', pd.concat([x, y], ignore_index=True))
    # Adding MultiIndex keys¶
    print('keys=[x,y] \r\n', pd.concat([x, y], keys=['x', 'y']))

    # Concatenation with joins
    df5 = make_df('ABC', [1, 2])
    df6 = make_df('BCD', [3, 4])
    print('x \r\n', df5)
    print('y \r\n', df6)
    print('concat \r\n', pd.concat([df5, df6]))
    print('join=inner \r\n', pd.concat([df5, df6], join='inner'))
    print('join_axes=[df.columns] \r\n', pd.concat([df5, df6], join_axes=[df5.columns]))

    # append
    print('append \r\n', df1.append(df2))
    print('df1 \r\n', df1)


def join():
    df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                        'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
    df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                        'hire_date': [2004, 2008, 2012, 2014]})
    df3 = pd.merge(df1, df2)
    print('df1: \r\n', df1, '\r\ndf2: \r\n', df2, '\r\ndf3 = pd.merge(df1, df2): \r\n', df3)

    # Many-to-one joins
    df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
                        'supervisor': ['Carly', 'Guido', 'Steve']})
    df34 = pd.merge(df3, df4)
    print('df4: \r\n', df4, '\r\npd.merge(df3, df5): \r\n', df34)

    # Many-to-many joins
    df5 = pd.DataFrame({'group': ['Accounting', 'Accounting',
                                  'Engineering', 'Engineering', 'HR', 'HR'],
                        'skills': ['math', 'spreadsheets', 'coding', 'linux',
                                   'spreadsheets', 'organization']})
    df15 = pd.merge(df1, df5)
    print('df5: \r\n', df5, '\r\npd.merge(df1, df5): \r\n', df15)

    pd.merge(df1, df2, on='employee')

    # The left_on and right_on keywords
    df6 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                        'salary': [70000, 80000, 120000, 90000]})
    df7 = pd.merge(df1, df6, left_on="employee", right_on="name")
    print('df6: \r\n', df6, '\r\n pd.merge(df1, df6,left_on=employee, right_on=name): \r\n', df7)
    print(df7.drop('name', axis=1)) # The result has a redundant column that we can drop

    # The left_index and right_index keywords
    df1a = df1.set_index('employee')
    df2a = df2.set_index('employee')
    print('\r\n df1a: \r\n', df1a, 'df2a: \r\n', df2a)
    m1 = pd.merge(df1a, df2a, left_index=True, right_index=True)
    print('merge(df1a, df2a, left_index=True, right_index=True) : \r\n', m1)
    df1a.join(df2a) # mplement the join() method, which performs a merge that defaults to joining on indices
    # mix indices and columns
    m2 = pd.merge(df1a, df6, left_index=True, right_on='name')
    print('merge(df1a, df6, left_index=True, right_on=name) : \r\n', m2)

    df8 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                        'food': ['fish', 'beans', 'bread']},
                       columns=['name', 'food'])
    df9 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                        'drink': ['wine', 'beer']},
                       columns=['name', 'drink'])
    print('df8: \r\n', df8, '\r\ndf9: \r\n', df9)
    print('pd.merge(df8, df9) \r\n', pd.merge(df8, df9))
    print('pd.merge(df8, df9, how=outer) \r\n', pd.merge(df8, df9, how='outer'))
    print('pd.merge(df8, df9, how=left) \r\n', pd.merge(df8, df9, how='left'))

    df10 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                        'rank': [1, 2, 3, 4]})
    df11 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                        'rank': [3, 1, 4, 2]})
    print('pd.merge(df10, df11,on="name") \r\n', pd.merge(df10, df11,  on="name"))
    print('pd.merge(df10, df11, on=name, suffixes=[_L, _R]) \r\n', pd.merge(df10, df11, on="name", suffixes=["_L", "_R"]))


if __name__ == '__main__':
    print('Numpy Version:', np.__version__)
    print('Pandas Version:', pd.__version__)
    # concatenation()
    join()
