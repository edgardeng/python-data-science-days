##
import numpy as np
import pandas as pd


def performance():
    rang = np.random.RandomState(42)
    x = rang.rand(1000000)
    y = rang.rand(1000000)
    # %timeit x + y  100 loops, best of 3: 3.39 ms per loop
    # %timeit np.fromiter((xi + yi for xi, yi in zip(x, y)), dtype=x.dtype, count=len(x))
    # 1 loop, best of 3: 266 ms per loop
    mask = (x > 0.5) & (y < 0.5)

    # import numexpr
    # mask_numexpr = numexpr.evaluate('(x > 0.5) & (y < 0.5)')
    # np.allclose(mask, mask_numexpr)


def efficient_eval():
    nrows, ncols = 100000, 100
    rng = np.random.RandomState(42)
    df1, df2, df3, df4 = (pd.DataFrame(rng.rand(nrows, ncols))
                          for i in range(4))
    # %timeit df1 + df2 + df3 + df4
    # %timeit pd.eval('df1 + df2 + df3 + df4')
    np.allclose(df1 + df2 + df3 + df4, pd.eval('df1 + df2 + df3 + df4'))

    df1, df2, df3, df4, df5 = (pd.DataFrame(rng.randint(0, 1000, (100, 3)))
                               for i in range(5))
    # 1. Arithmetic operators
    result1 = -df1 * df2 / (df3 + df4) - df5
    result2 = pd.eval('-df1 * df2 / (df3 + df4) - df5')
    np.allclose(result1, result2)

    # 2. Comparison operators
    result1 = (df1 < df2) & (df2 <= df3) & (df3 != df4)
    result2 = pd.eval('df1 < df2 <= df3 != df4')
    np.allclose(result1, result2)

    # 3. Bitwise operators
    result1 = (df1 < 0.5) & (df2 < 0.5) | (df3 < df4)
    result2 = pd.eval('(df1 < 0.5) & (df2 < 0.5) | (df3 < df4)')
    np.allclose(result1, result2)
    result3 = pd.eval('(df1 < 0.5) and (df2 < 0.5) or (df3 < df4)')
    np.allclose(result1, result3)

    # 4. Object attributes and indices
    result1 = df2.T[0] + df3.iloc[1]
    result2 = pd.eval('df2.T[0] + df3.iloc[1]')
    np.allclose(result1, result2)

    # 5. Column-Wise Operations
    df = pd.DataFrame(rng.rand(1000, 3), columns=['A', 'B', 'C'])
    print(df.head())
    result1 = (df['A'] + df['B']) / (df['C'] - 1)
    result2 = pd.eval("(df.A + df.B) / (df.C - 1)")
    # print(result2)
    np.allclose(result1, result2)
    result3 = df.eval('(A + B) / (C - 1)')
    np.allclose(result1, result3)

    # 6. Assignment
    df.eval('D = (A + B) / C', inplace=True)
    print(df.head())
    df.eval('D = (A - B) / C', inplace=True)
    print(df.head())

    # 7. Local variables
    column_mean = df.mean(1)
    result1 = df['A'] + column_mean
    result2 = df.eval('A + @column_mean')
    np.allclose(result1, result2)


def efficient_query():
    rang = np.random.RandomState(42)
    df = pd.DataFrame(rang.rand(100, 3), columns=['A', 'B', 'C'])
    result1 = df[(df.A < 0.5) & (df.B < 0.5)]
    result2 = pd.eval('df[(df.A < 0.5) & (df.B < 0.5)]')
    np.allclose(result1, result2)
    # filtering operation, you can use the query() method:
    result2 = df.query('A < 0.5 and B < 0.5')
    np.allclose(result1, result2)
    Cmean = df['C'].mean()
    result1 = df[(df.A < Cmean) & (df.B < Cmean)]
    result2 = df.query('A < @Cmean and B < @Cmean')
    np.allclose(result1, result2)


if __name__ == '__main__':
    print('Numpy Version:', np.__version__)
    print('Pandas Version:', pd.__version__, '\r\n')
    # simple_example()
    efficient_eval()