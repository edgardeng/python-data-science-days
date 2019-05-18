## Day 16 Pandas Data Selection

### Data Selection in Series

A Series builds on this dictionary-like interface and provides array-style item selection via the same basic mechanisms as NumPy arrays – that is, slices, masking, and fancy indexing.

```python
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
```

#### Special Indexers

Pandas provides some special indexer attributes that explicitly expose certain indexing schemes.

* The __loc__ attribute allows indexing and slicing that always references the explicit index

* The __iloc__ attribute allows indexing and slicing that always references the implicit Python-style index

* __ix__, is a hybrid of the two, and for Series objects is equivalent to standard []-based indexing. 
    
### Data Selection in DataFrame

In particular, you should avoid the temptation to try column assignment via attribute (i.e., use data['pop'] = z rather than data.pop = z).

Like with the ``Series`` objects discussed earlier, this dictionary-style syntax can also be used to modify the object,

```python
    area = pd.Series({'California': 423967, 'Texas': 695662,
                      'New York': 141297, 'Florida': 170312,
                      'Illinois': 149995})
    pop = pd.Series({'California': 38332521, 'Texas': 26448193,
                     'New York': 19651127, 'Florida': 19552860,
                     'Illinois': 12882135})
    data = pd.DataFrame({'area':area, 'pop':pop})
    print('data.area is data[\'area\']', data.area is data['area']) # TRUE
    print('data.pop is data[\'pop\']', data.pop is data['pop']) # FALSE the ``DataFrame`` has a ``pop()`` method
    data['density'] = data['pop'] / data['area']
    print('data: \r\n', data)
```

> NOTE THAT:

* if the column names are not strings, or if the column names conflict with methods of the ``DataFrame``, this attribute-style access is not possible.

* the ``DataFrame`` has a ``pop()`` method, so ``data.pop`` will point to this rather than the ``"pop"`` column:

In particular, you should avoid the temptation to try column assignment via attribute (i.e., use data['pop'] = z rather than data.pop = z).

```python
    print('data.iloc[:3, :2]:\r\n', data.iloc[:3, :2])
    print('data.iloc[:Illinois, :pop]:\r\n', data.loc[:'Illinois', :'pop'])
    # ix -- a hybrid of these two approaches
    print('data.data.ix[:3, :\'pop\']:\r\n', data.ix[:3, :'pop'])
    # combine masking and fancy indexing
    print('data.loc[data.density > 100, [\'pop\', \'density\']]:\r\n')
    print(data.loc[data.density > 100, ['pop', 'density']])
    data.iloc[0, 2] = 90
    print(data)
```    
    
#### Additional indexing conventions

```python
data['Florida':'Illinois']

data[1:3]

data[data.density > 100]

```
* while indexing refers to columns, slicing refers to rows:

* direct masking operations are also interpreted row-wise rather than column-wise:

---
   
### Operating on Data

#### Ufuncs: Index Preservation 通用函数: 索引保持

Because Pandas is designed to work with NumPy, any NumPy ufunc will work on Pandas Series and DataFrame objects.

```python
    rng = np.random.RandomState(42)
    ser = pd.Series(rng.randint(0, 10, 4))
    df = pd.DataFrame(rng.randint(0, 10, (3, 4)), columns=['A', 'B', 'C', 'D'])
    print('Series:\r\n', ser)
    print('np.exp(ser):\r\n', np.exp(ser))
    print('DataFrame:\r\n', df)
    print('np.sin(df * np.pi / 4):\r\n', np.sin(df * np.pi / 4))
```

#### UFuncs: Index Alignment 索引对齐

```python
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
```

The following table lists Python operators and their equivalent Pandas object methods:

| Python Operator | Pandas Method(s)                      |
|-----------------|---------------------------------------|
| ``+``           | ``add()``                             |
| ``-``           | ``sub()``, ``subtract()``             |
| ``*``           | ``mul()``, ``multiply()``             |
| ``/``           | ``truediv()``, ``div()``, ``divide()``|
| ``//``          | ``floordiv()``                        |
| ``%``           | ``mod()``                             |
| ``**``          | ``pow()``                             |

#### Ufuncs: Operations Between DataFrame and Series 数据操作

```python
    data = rng.randint(10, size=(3, 4))
    print(data - data[0])
    df_2 = pd.DataFrame(data, columns=list('ABCD'))
    print(df_2 - df_2.iloc[0])  # operates row-wise
    print(df_2.subtract(df_2['A'], axis=0)) # operate column-wise
    half_row = df_2.iloc[0, ::2]
    print(df_2 - half_row)
```

---

### Handling Missing Data

>  missing data in general as null, NaN, or NA values.

#### None: Pythonic missing data

None, a Python singleton object that is often used for missing data.

None cannot be used in any arbitrary NumPy/Pandas array, but only in arrays with data type 'object'

```python
def sum_object():
    print(np.arange(1E6, dtype='object').sum())


def sum_int():
    print(np.arange(1E6, dtype='int').sum())

val = np.array([1, None, 3, 4])
print("dtype = object")
timeit.timeit(sum_object, number=1)
print("dtype = int")
timeit.timeit(sum_int, number=1)
print('val.sum', val.sum()) # TypeError 
```

#### ``NaN``: Missing numerical data

```python
    val_2 = np.array([1, np.nan, 3, 4])
    print('val_e.dtype:', val_2.dtype)
    print('1 + np.nan:', 1 + np.nan)
    print('0 *  np.nan:', 0 * np.nan)
    print(np.nansum(val_2), np.nanmin(val_2), np.nanmax(val_2)) # 8, 1, 4
    print(val_2.sum(), val_2.min(), val_2.max())  # nan, nan, nan
    
```

``NaN`` is specifically a floating-point value; there is no equivalent NaN value for integers, strings, or other types.

#### NaN and None in Pandas

table of the upcasting conventions in Pandas when NA values are introduced:

|Typeclass     | Conversion When Storing NAs | NA Sentinel Value      |
|--------------|-----------------------------|------------------------|
| ``floating`` | No change                   | ``np.nan``             |
| ``object``   | No change                   | ``None`` or ``np.nan`` |
| ``integer``  | Cast to ``float64``         | ``np.nan``             |
| ``boolean``  | Cast to ``object``          | ``None`` or ``np.nan`` |

> NOTE: in Pandas, string data is always stored with an ``object`` dtype.

#### Operating on Null Values

As we have seen, Pandas treats ``None`` and ``NaN`` as essentially interchangeable for indicating missing or null values.

To facilitate this convention, there are several useful methods for detecting, removing, and replacing null values in Pandas data structures.

* ``isnull()``: Generate a boolean mask indicating missing values
* ``notnull()``: Opposite of ``isnull()``
* ``dropna()``: Return a filtered version of the data
* ``fillna()``: Return a copy of the data with missing values filled or imputed

#### Detecting 、 Dropping and Filling null values

Pandas data structures have two useful methods for detecting null data: ``isnull()`` and ``notnull()``.
Either one will return a Boolean mask over the data. 

```python
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
```


For a ``DataFrame``：

* By default, ``dropna()`` will drop all rows in which *any* null value is present:
 
* We can also specify ``how='all'``, which will only drop rows/columns that are *all* null values:

* For finer-grained control, the ``thresh`` parameter lets you specify a minimum number of non-null values for the row/column to be kept:

__filling__

* fill NA entries with a single value, such as zero: `fillna(0)`

* specify a forward-fill to propagate the previous value forward:`fillna(method='ffill')`

* specify a back-fill to propagate the next values backward: `fillna(method='bfill')`

* specify an ``axis`` along which the fills take place: `fillna(method='ffill', axis=1)`

> Note: if a previous value is not available during a forward fill, the NA value remains.

---

### Hierarchical Indexing 分层索引


####  A Multiply Indexed Series 多重索引


With this indexing scheme, you can straightforwardly index or slice the series based on this multiple index:
#%%
pop[('California', 2010):('Texas', 2000)]


#### MultiIndex as extra dimension

Each extra level in a multi-index represents an extra dimension of data; taking advantage of this property gives us much more flexibility in the types of data we can represent


####  Methods of MultiIndex Creation

```python

df = pd.DataFrame(np.random.rand(4, 2),
                  index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],
                  columns=['data1', 'data2'])

# pass a dictionary with appropriate tuples as keys

data = {('California', 2000): 33871648,
        ('California', 2010): 37253956,
        ('Texas', 2000): 20851820,
        ('Texas', 2010): 25145561,
        ('New York', 2000): 18976457,
        ('New York', 2010): 19378102}
pd.Series(data)

```

#### Explicit MultiIndex constructors

For more flexibility in how the index is constructed, you can instead use the class method constructors available in the ``pd.MultiIndex``.
For example, as we did before, you can construct the ``MultiIndex`` from a simple list of arrays giving the index values within each level:
```python

pd.MultiIndex.from_arrays([['a', 'a', 'b', 'b'], [1, 2, 1, 2]])

# from a list of tuples 
pd.MultiIndex.from_tuples([('a', 1), ('a', 2), ('b', 1), ('b', 2)])

# from a Cartesian product of single indices:
pd.MultiIndex.from_product([['a', 'b'], [1, 2]])

#  using its internal encoding by passing `levels` and `labels`
pd.MultiIndex(levels=[['a', 'b'], [1, 2]], labels=[[0, 0, 1, 1], [0, 1, 0, 1]])
```

#### MultiIndex level names

This can be accomplished by passing the ``names`` argument to any of the above ``MultiIndex`` constructors, or by setting the ``names`` attribute of the index after the fact:`pop.index.names = ['state', 'year']`

#### MultiIndex for columns

```python
    index = pd.MultiIndex.from_product([[2013, 2014], [1, 2]], names=['year', 'visit'])
    columns = pd.MultiIndex.from_product([['Bob', 'Guido', 'Sue'], ['HR', 'Temp']], names=['subject', 'type'])
    data = np.round(np.random.randn(4, 6), 1) # mock some data
    data[:, ::2] *= 10
    data += 37
    
    # create the DataFrame
    health_data = pd.DataFrame(data, index=index, columns=columns)
    print(health_data)
    print(health_data['Guido'])
    
```

#### Multiply indexed Series

```python
    print(series_pop['California', 2000])
    print(series_pop.loc['California':'New York']) # partial indexing
    print(series_pop[:, 2000])
    print(series_pop[series_pop > 22000000]) #  Boolean masks:
    print(series_pop[['California', 'Texas']]) # fancy indexing
    
```

#### Multiply indexed DataFrames

```python
    print(health_data['Guido', 'HR']) # index
    # ``loc``, ``iloc``, and ``ix`` indexers
    print(health_data.iloc[:2, :2])
    print(health_data.loc[:, ('Bob', 'HR')])
    # print(health_data.loc[(:, 1), (:, 'HR')]) # these index tuples is not especially convenient;
    idx = pd.IndexSlice
    print(health_data.loc[idx[:, 1], idx[:, 'HR']])
```

#### Sorted and unsorted indices

*Many of the ``MultiIndex`` slicing operations will fail if the index is not sorted.*

For various reasons, partial slices and other similar operations require the levels in the ``MultiIndex`` to be in sorted (i.e., lexographical) order.

Pandas provides a number of convenience routines to perform this type of sorting; examples are the ``sort_index()`` and ``sortlevel()`` methods of the ``DataFrame``.

```python

```

#### Stacking and unstacking indices

```python
    pop.unstack(level=0)
    pop.unstack(level=1)
    pop.unstack().stack()
```

### Index setting and resetting

Another way to rearrange hierarchical data is to turn the index labels into columns; this can be accomplished with the ``reset_index`` method.
Calling this on the population dictionary will result in a ``DataFrame`` with a *state* and *year* column holding the information that was formerly in the index.
For clarity, we can optionally specify the name of the data for the column representation:

```python
_pop_flat = pop.reset_index(name='population')

pop_flat.set_index(['state', 'year'])_

```

Often when working with data in the real world, the raw input data looks like this and it's useful to build a ``MultiIndex`` from the column values.
This can be done with the ``set_index`` method of the ``DataFrame``, which returns a multiply indexed ``DataFrame``:

In practice, I find this type of reindexing to be one of the more useful patterns when encountering real-world datasets.




