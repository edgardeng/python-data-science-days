## Day 15 Introduction to Pandas

> Pandas is a newer package built on top of NumPy, and provides an efficient implementation of a DataFrame. 

DataFrames are essentially multidimensional arrays with attached row and column labels, and often with heterogeneous types and/or missing data. 
As well as offering a convenient storage interface for labeled data, Pandas implements a number of powerful data operations familiar to users of both database frameworks and spreadsheet programs.

### Pandas Series Object

A Pandas Series is a one-dimensional array of indexed data.

```python
import numpy as np
import pandas as pd
data = pd.Series([0.25, 0.5, 0.75, 1.0])
print(data)
print(data)

```

The Series wraps both a sequence of values and a sequence of indices, which we can access with the values and index attributes. 

##### Series as generalized NumPy array

while the Numpy Array has an implicitly defined integer index used to access the values, the Pandas Series has an explicitly defined index associated with the values.

```python
    data_2 = pd.Series([0.25, 0.5, 0.75, 1.0], index=[3, 5, 6, 4])
    print('data[5] = ', data_2[5])
    print('data[:5] = ', data_2[:5])
```

#### Series as specialized dictionary

```python
    dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    data_3 = pd.Series(dict)
    print('data[\'a\'] = ', data_3['a'])
    print('data[\'a\':\'c\'] = ', data_3['a': 'c'])
```

#### Constructing Series objects

a few ways of constructing a Pandas Series:

```python
pd.Series([2, 4, 6])

pd.Series(5, index=[100, 200, 300])

pd.Series({2:'a', 1:'b', 3:'c'})

pd.Series({2:'a', 1:'b', 3:'c'}, index=[3, 2])
```

### The Pandas DataFrame Object

the DataFrame can be thought of either as a generalization of a NumPy array, or as a specialization of a Python dictionary. 

#### DataFrame as a array or dictionary

DataFrame can be thought of as a generalization of a two-dimensional NumPy array, where both the rows and columns have a generalized index for accessing the data.

Similarly, we can also think of a DataFrame as a specialization of a dictionary. 

```python
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
```

#### Constructing DataFrame objects

```python
# from a single Series:
pd.DataFrame(population, columns=['population'])

# from a list of dictionaries
data = [{'a': i, 'b': 2 * i} for i in range(3)]
pd.DataFrame(data)

pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]) #  if some keys are missing, Pandas will fill them in with NaN

# from a dictionary of Series objects
pd.DataFrame({'population': population, 'area': area})

# from a two-dimensional NumPy array
pd.DataFrame(np.random.rand(3, 2), columns=['foo', 'bar'], index=['a', 'b', 'c'])
             
# from a NumPy structured array          
a = np.zeros(3, dtype=[('A', 'i8'), ('B', 'f8')])
pd.DataFrame(a)

```

### The Pandas Index Object

Both the Series and DataFrame objects contain an explicit index that lets you reference and modify data.
 
This Index object is an interesting structure in itself, and it can be thought of either as __an immutable array__ or as __an ordered set__ (technically a multi-set, as Index objects may contain repeated values). 

```python
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
    
```
