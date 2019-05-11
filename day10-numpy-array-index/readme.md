## day 10 Numpy Array Index

### Exploring Fancy Indexing

Fancy indexing is conceptually simple: it means passing an array of indices to access multiple array elements at once. 

```python
    import numpy as np
    x = np.arange(10)
    print('x = ', x)
    print([x[3], x[7], x[2]])
    ind = [3, 7, 4]
    print('x[ind] = ', x[ind])
    ind2 = np.array([[3, 7],
                    [4, 5]])
    print('x[ind2] = ', x[ind2])

    y = np.arange(12).reshape((3, 4))
    row = np.array([0, 1, 2])
    col = np.array([2, 1, 3])
    print('y = ', y)
    print('row = ', row, 'col = ', col)
    print('y[row, col] = ', y[row, col])
    print('x[row[:, np.newaxis], col] = ', y[row[:, np.newaxis], col])
    print('row[:, np.newaxis] * col = ', row[:, np.newaxis] * col)
    
```

if we combine a column vector and a row vector within the indices, we get a two-dimensional result:

### Combined Indexing

For even more powerful operations, fancy indexing can be combined with the other indexing schemes

```python
    x = np.arange(12).reshape((3, 4))
    print('x = ', x)
    print('x[2, [2, 0, 1]] = ', x[2, [2, 0, 1]])
    print('x[1:, [2, 0, 1]] = ', x[1:, [2, 0, 1]])
    mask = np.array([1, 0, 1, 0], dtype=bool)
    row = np.array([0, 1, 2])
    print('x[row[:, np.newaxis], mask]', x[row[:, np.newaxis], mask])
```

### Example

#### Selecting Random Points

```python
def select_random():
    mean = [0, 0]
    cov = [[1, 2], [2, 5]]
    x = np.random.multivariate_normal(mean, cov, 100)
    print('x.shape', x.shape)
    # choosing 20 random indices with no repeats
    indices = np.random.choice(x.shape[0], 20, replace=False)
    print('indices = ', indices)
    # selection = x[indices]  # fancy indexing here
    print(x[indices].shape)
```

#### Modifying Values

Just as fancy indexing can be used to access parts of an array, it can also be used to modify parts of an array.

```python
def modify_value():
    x = np.arange(10)
    print('x =', x)
    i = np.array([2, 1, 8, 4])
    x[i] = 99
    print('after x[i]=99 :', x)
    x[i] -= 10
    print('after x[i]-=10 :', x)
    x = np.arange(10)

    y = np.zeros(10)
    print('before y =', y)
    y[[0, 0]] = [4, 6]
    print('after y[[0, 0]] = [4, 6] :', y)
    i = [2, 3, 3, 4, 4, 4]
    y[i] += 1
    print('after y[i] += 1 :', y)
    z = np.zeros(10)
    np.add.at(z, i, 1)
    print('after z[i] += 1 :', z)
```

The result of this operation is to first assign x[0] = 4, followed by x[0] = 6. The result, of course, is that x[0] contains the value 6.

Conceptually, because x[i] += 1 is meant as a shorthand of x[i] = x[i] + 1. x[i] + 1 is evaluated, and then the result is assigned to the indices in x. With this in mind, it is not the augmentation that happens multiple times, but the assignment, which leads to the rather nonintuitive results.

For this, we can use the at() method of ufuncs (available since NumPy 1.8), 

#### Binning Data

```python

def binning_data():
    x = np.random.randn(50)
    # compute a histogram by hand
    bins = np.linspace(-5, 5, 20)
    counts = np.zeros_like(bins)
    i = np.searchsorted(bins, x)
    np.add.at(counts, i, 1)

    y = np.random.randn(1000000)
    t1 = time.time()
    # compute a histogram by hand by numpy
    counts, edges = np.histogram(y, bins)
    t2 = time.time()
    np.add.at(counts, np.searchsorted(bins, x), 1)
    t3 = time.time()
    
```

NumPy's algorithm is more flexible, and particularly is designed for better performance when the number of data points becomes large:
