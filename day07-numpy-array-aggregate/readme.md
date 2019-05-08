## day 7 Numpy Array Function For Aggregations

NumPy has fast built-in aggregation functions for working on arrays;

### Sum, Min, Max

```python
    import numpy as np
    L = np.random.random(50)
    print('Array:', L, '\r\n')
    print('python sum:', sum(L))
    print('numpy sum:', np.sum(L))
    print('python min:', min(L))
    print('numpy min:', np.min(L))
    print('python max:', max(L))
    print('numpy max:', np.max(L))
    print('min:', L.min(), 'max:', L.max(), 'sum:', L.sum())
```

Python itself can do this using the built-in sum function:

NumPy's version of the operation is computed much more quickly:

For min, max, sum, and several other NumPy aggregates, a shorter syntax is to use methods of the array object itself:

```python
    M = np.random.random((4, 5))
    print('Array:', M, '\r\n')
    print('min:', M.min(), 'max:', M.max(), 'sum:', M.sum())
    print('min(axis=0):', M.min(axis=0))
    print('max(axis=1):', M.max(axis=1))
```

By default, each NumPy aggregation function will return the aggregate over the entire array:

The axis keyword specifies the dimension of the array that will be collapsed, rather than the dimension that will be returned.

### Other aggregation functions

a list of useful aggregation functions available in NumPy:

|Function Name	|NaN-safe Version	|Description|
| :----         | :---- | :---- |
|np.sum	        |np.nansum	    |Compute sum of elements |
|np.prod	    |np.nanprod	    |Compute product of elements|
|np.mean	    |np.nanmean	    |Compute mean of elements|
|np.std	        |np.nanstd	    |Compute standard deviation|
|np.var	        |np.nanvar	    |Compute variance|
|np.min	        |np.nanmin	    |Find minimum value|
|np.max	        |np.nanmax	    |Find maximum value|
|np.argmin	    |np.nanargmin	|Find index of minimum value|
|np.argmax	    |np.nanargmax	|Find index of maximum value|
|np.median	    |np.nanmedian	|Compute median of elements|
|np.percentile	|np.nanpercentile	|Compute rank-based statistics of elements|
|np.any         |N/A	        |Evaluate whether any elements are true|
|np.all	        |N/A	        |Evaluate whether all elements are true|

#### Example

```python
    l = np.random.randint(100, size=20)
    print('Array:', l, '\r\n')
    print("Mean :       ", l.mean())
    print("Standard deviation:", l.std())
    print("Minimum :    ", l.min())
    print("Maximum :    ", l.max())
    print("25th percentile:   ", np.percentile(l, 25))
    print("Median:            ", np.median(l))
    print("75th percentile:   ", np.percentile(l, 75))
    b = l > 50
    print("has bigger :", b.any())
    print("all bigger :", b.all())
```
