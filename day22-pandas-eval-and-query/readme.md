## High-Performance Pandas: `eval() and query()`

### Compound Expressions 复合表达式


#### efficient eval 高效使用eval函数

> The eval() version of this expression is about 50% faster (and uses much less memory), while giving the same result:

#### Operations supported by pd.eval eval函数支持的操作

```python
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
```

### query() Method

```python
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
```

When considering whether to use these functions, there are two considerations: computation time and memory use. 
Memory use is the most predictable aspect. 
As already mentioned, every compound expression involving NumPy arrays or Pandas DataFrames will result in implicit creation of temporary arrays

```python
x = df[(df.A < 0.5) & (df.B < 0.5)]
```

Is roughly equivalent to this:

```python
tmp1 = df.A < 0.5
tmp2 = df.B < 0.5
tmp3 = tmp1 & tmp2
x = df[tmp3]
```



