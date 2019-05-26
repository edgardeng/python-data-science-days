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


if __name__ == '__main__':
    print('Numpy Version:', np.__version__)
    print('Pandas Version:', pd.__version__)
    concatenation()
