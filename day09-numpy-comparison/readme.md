## day 9 Numpy Comparison

Masking comes up when you want to extract, modify, count, or otherwise manipulate values in an array based on some criterion: for example, you might wish to count all values greater than a certain value, or perhaps remove all outliers that are above some threshold. 

In NumPy, Boolean masking is often the most efficient way to accomplish these types of tasks.

### Comparison
 
NumPy implements comparison operators such as < (less than) and > (greater than) as element-wise ufuncs. The result of these comparison operators is always an array with a Boolean data type. 

```python
    a = np.arange(10)
    print('a = ', a)
    print('less than :', a < 5)
    print('greater than :', a > 5)
    print('less and equal :', a <= 5)
    print('greater and equal :', a >= 5)
    print('equal :', a == 5)
    print('not equal :', a != 5)
    print('even :',  a % 2 == 0)
    b = np.random.randint(10, size=(2, 3))
    print('2 dims less than :', b < 5)
```

### Working with Boolean Arrays

To count the number of True entries in a Boolean array, np.count_nonzero is useful:

Another way to get at this information is to use np.sum; 

The benefit of sum() is that like with other NumPy aggregation functions, this summation can be done along rows or columns as well:

```python

    a = np.random.randint(10, size=(3, 4))
    print('a = ', a)
    print('count:', np.count_nonzero(a < 6))
    print('sum:', np.sum(a < 6))
    print('count in each row:', np.sum(a < 6, axis=1))
    print('have >8: ', np.any(a > 8))
    print('all >8: ', np.all(a > 8))
    print('row all >8', np.all(a > 8, axis=1))

    print('count 2-5:', np.sum((a > 2) & (a < 5)))
    print('count 2-5', np.sum(~((a <= 2) | (a >= 5))))

```
The following table summarizes the bitwise Boolean operators and their equivalent ufuncs:

|Operator|	Equivalent ufunc|
|:----|:----|
|&	| np.bitwise_and  |
|^	| np.bitwise_xor  |
|&#124;	| np.bitwise_or   |
|~	| np.bitwise_not  |
		
### Boolean Arrays as Mask

A more powerful pattern is to use Boolean arrays as masks, to select particular subsets of the data themselves.
 
```python
    print('< 5 mask: ', a[a < 5])
    print('< 5 mask median:', np.median(a[a < 5]))
    more = a > 5
    even = a % 2 == 0
    print('> 5 & even mask median:', np.median(a[more & even]))

```
By combining Boolean operations, masking operations, and aggregates, we can very quickly answer these sorts of questions for our dataset


### Keywords (and/or) Vs Operators (&/|)

```python

    print('bool(42) =', bool(42), 'bool(0) =', bool(0))
    print('bool(42 and 0) =', bool(42 and 0), 'bool(42 or 0) =', bool(42 or 0))
    print('bin(42) =', bin(42), 'bin(59) =', bin(59))
    print('bin(42 & 59) =', bin(42 & 59), 'bin(42 | 0) =', bin(42 | 59))

    a = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
    b = np.array([1, 1, 1, 0, 1, 1], dtype=bool)
    print('A | B = ', a | b)
    # print('A or B = ', a or b) # ValueError
    x = np.arange(10)
    print('(x > 4) & (x < 8)', (x > 4) & (x < 8))
    # print('(x > 4) and (x < 8)', (x > 4) and (x < 8)) # ValueError:
```

The difference is this: and and or gauge the truth or falsehood of entire object, while & and | refer to bits within each object.
