## day 11 Numpy Array Sort

### Sort Algorithm

These sort algorithms are a favorite topic in introductory computer science courses:  *insertion sorts*, *selection sorts*, *merge sorts*, *quick sorts*, *bubble sorts*, and many, many more.

All are means of accomplishing a similar task: sorting the values in a list or array.

```python
def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x
```

### Fast Sorting in NumPy

> np.sort and np.argsort

To return a sorted version of the array without modifying the input, you can use ``np.sort``:

A related function is ``argsort``, which instead returns the *indices* of the sorted elements:

```python
    x = np.array([1, 3, 2, 7, 10, 5, 9, 8, 6, 4])
    print('x = ', x)
    x.sort()
    print('after sorted: ', x)
    y = np.array([1, 3, 2, 7, 10, 5, 9, 8, 6, 4])
    i = np.argsort(y)
    print('after argsort y = ', y)
    print('indice : ', i)
    print('y[i] = ', y[i])
    
```

### Sorting along rows or columns

Keep in mind that this treats each row or column as an independent array, and any relationships between the row or column values will be lost!

```python
    x = np.random.randint(0, 10, (4, 6))
    print('x = ', x)
    print('np.sort(x, axis=0) ', np.sort(x, axis=0))
```

### Partial Sorts: Partitioning

```python
 def part_sort():
     x = np.array([7, 2, 3, 8, 6, 5, 4, 0, 9, 10])
     print('np.partition(x, 3):', np.partition(x, 3))
     y = np.random.randint(0, 10, (5, 5))
     print('np.partition(y, 2, axis=0)', np.partition(y, 2, axis=0))
```

NumPy provides this in the np.partition function. np.partition takes an array and a number *K; the result is a new array with the smallest K values to the left of the partition, and the remaining values to the right

#### k-Nearest Neighbors K领域算法

Let's quickly see how we might use this argsort function along multiple axes to find the nearest neighbors of each point in a set. 

```python
    # creating a random set of 10 points on a two-dimensional plane.
    x = np.random.rand(10, 2)
    # compute the distance between each pair of points.
    dist_sq = np.sum((x[:, np.newaxis, :] - x[np.newaxis, :, :]) ** 2, axis=-1)
    # for each pair of points, compute differences in their coordinates
    differences = x[:, np.newaxis, :] - x[np.newaxis, :, :]
    print('differences.shape', differences.shape)
    # square the coordinate differences
    sq_differences = differences ** 2
    print('sq_differences.shape', sq_differences.shape)
    # sum the coordinate differences to get the squared distance
    dist_sq = sq_differences.sum(-1)
    print('dist_sq.shape', dist_sq.shape)
    dist_sq.diagonal()
    nearest = np.argsort(dist_sq, axis=1)
    print(nearest)
    K = 2
    nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)
    print('nearest_partition', nearest_partition)
```

#### Aside: Big-O Notation

Big-O notation is a means of describing how the number of operations required for an algorithm scales as the input grows in size.
 To use it correctly is to dive deeply into the realm of computer science theory, and to carefully distinguish it from the related small-o notation, big-
θ notation, big-Ω notation, and probably many mutant hybrids thereof. 
 
 Big-O notation, in this loose sense, tells you how much time your algorithm will take as you increase the amount of data. If you have an 
 O[N](read "order N") algorithm that takes 1 second to operate on a list of length N*=1,000, then you should expect it to take roughly 5 seconds for a list of length *N=5,000. If you have an 
 O[N2](read "order N* squared") algorithm that takes 1 second for *N=1000, then you should expect it to take about 25 seconds for N=5000.
  
