## Day 17 Pandas Data Operation

### Combining Datasets

#### Recall: Concatenation of NumPy Arrays

`np.concatenate`: combine the contents of two or more arrays into a single array:

The first argument is a list or tuple of arrays to concatenate.
 
Additionally, it takes an axis keyword that allows you to specify the axis along which the result will be concatenated:

```python
    x = [1, 2, 3]
    y = [4, 5, 6]
    z = [7, 8, 9]
    print(np.concatenate([x, y, z])) # [1 2 3 4 5 6 7 8 9]
    x = [[1, 2],
         [3, 4]]
    print(np.concatenate([x, x], axis=1)) #  [[1 2 1 2] [3 4 3 4]]
```

#### Concatenation with pd.concat

pd.concat() can be used for a simple concatenation of Series or DataFrame objects

```python
pd.concat(objs, axis=0, join='outer', join_axes=None, ignore_index=False,
          keys=None, levels=None, names=None, verify_integrity=False,
          copy=True)
```

```python
import pandas as pd
def make_df(cols, ind):
    """Quickly make a DataFrame"""
    data = {c: [str(c) + str(i) for i in ind]
            for c in cols}
    return pd.DataFrame(data, ind)
    
ser1 = pd.Series(['A', 'B', 'C'], index=[1, 2, 3])
ser2 = pd.Series(['D', 'E', 'F'], index=[4, 5, 6])
pd.concat([ser1, ser2])

df1 = make_df('AB', [1, 2])
df2 = make_df('AB', [3, 4])
pd.concat([df1, df2])

df3 = make_df('AB', [0, 1])
df4 = make_df('CD', [0, 1])
pd.concat([df3, df4], axis=1)

```

Pandas concatenation preserves indices, even if the result will have __duplicate indices__!

```python
x = make_df('AB', [0, 1])
y = make_df('AB', [2, 3])
y.index = x.index  # make duplicate indices!
pd.concat([x, y])

# Catching the repeats as an error
try:
    pd.concat([x, y], verify_integrity=True)
except ValueError as e:
    print("ValueError:", e)
# Ignoring the index
pd.concat([x, y], ignore_index=True)
# Adding MultiIndex keys
pd.concat([x, y], keys=['x', 'y'])

```

In practice, data from different sources might have different sets of column names, and pd.concat offers several options in this case.


By default, the entries for which no data is available are filled with NA values.

```python
df5 = make_df('ABC', [1, 2])
df6 = make_df('BCD', [3, 4])
pd.concat([df5, df6])

# the join is a union of the input columns (join='outer'), but we can change this to an intersection of the columns using join='inner':
pd.concat([df5, df6], join='inner')
# specify that the returned columns 
pd.concat([df5, df6], join_axes=[df5.columns])

```



#### The append() method¶

Series and DataFrame objects have an append method that can accomplish the same thing. For example, rather than calling pd.concat([df1, df2]), you can simply call df1.append(df2)

```python
df1.append(df2)
```
> Note: 
append() method in Pandas does not modify the original object–instead it creates a new object with the combined data.

     
     