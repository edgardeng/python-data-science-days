## Day 17 Pandas Data Operation

### Combining Datasets

#### Concatenation of NumPy Arrays

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

### Joins

The pd.merge() function implements a number of types of joins: the one-to-one, many-to-one, and many-to-many joins. 
     
```python
# One-to-one joins
df1 = pd.DataFrame({'employee': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'group': ['Accounting', 'Engineering', 'Engineering', 'HR']})
df2 = pd.DataFrame({'employee': ['Lisa', 'Bob', 'Jake', 'Sue'],
                    'hire_date': [2004, 2008, 2012, 2014]})
df3 = pd.merge(df1, df2)

# Many-to-one joins
df4 = pd.DataFrame({'group': ['Accounting', 'Engineering', 'HR'],
                    'supervisor': ['Carly', 'Guido', 'Steve']})
pd.merge(df3, df4)

# Many-to-many joins
df5 = pd.DataFrame({'group': ['Accounting', 'Accounting',
                              'Engineering', 'Engineering', 'HR', 'HR'],
                    'skills': ['math', 'spreadsheets', 'coding', 'linux',
                               'spreadsheets', 'organization']})
pd.merge(df1, df5)

```     

#### Specification of the Merge Key

```python
# The on keyword
pd.merge(df1, df2, on='employee')

# The left_on and right_on keywords
df3 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'salary': [70000, 80000, 120000, 90000]})
df6 = pd.merge(df1, df3, left_on="employee", right_on="name")

df6.drop('name', axis=1) # The result has a redundant column that we can drop 

# The left_index and right_index keywords
df1a = df1.set_index('employee')
df2a = df2.set_index('employee')
pd.merge(df1a, df2a, left_index=True, right_index=True)
df1a.join(df2a) # mplement the join() method, which performs a merge that defaults to joining on indices

# mix indices and columns
pd.merge(df1a, df3, left_index=True, right_on='name')

```

Most simply, specify the name of the key column using the on keyword, which takes a column name or a list of column names

At times you may wish to merge two datasets with different column names;  In this case, we can use the left_on and right_on keywords to specify the two column names

#### Specifying Set Arithmetic for Joins

```python
df6 = pd.DataFrame({'name': ['Peter', 'Paul', 'Mary'],
                    'food': ['fish', 'beans', 'bread']},
                   columns=['name', 'food'])
df7 = pd.DataFrame({'name': ['Mary', 'Joseph'],
                    'drink': ['wine', 'beer']},
                   columns=['name', 'drink'])
pd.merge(df6, df7)
pd.merge(df6, df7, how='outer')

pd.merge(df6, df7, how='left')

```
Merge two datasets , By default, the result contains the intersection of the two sets of inputs; 

this is what is known as an inner join. We can specify this explicitly using the how keyword, which defaults to "inner"

Other options for the how keyword are 'outer', 'left', and 'right'. 

#### Overlapping Column Names

Because the output would have two conflicting column names, the merge function automatically appends a suffix _x or _y to make the output columns unique. 

If these defaults are inappropriate, it is possible to specify a custom suffix using the suffixes keyword
 
```python
df8 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'rank': [1, 2, 3, 4]})
df9 = pd.DataFrame({'name': ['Bob', 'Jake', 'Lisa', 'Sue'],
                    'rank': [3, 1, 4, 2]})
pd.merge(df8, df9, on="name")
pd.merge(df8, df9, on="name", suffixes=["_L", "_R"])
```
