## day 8 Numpy Array Broadcasting

Another means of vectorizing operations is to use NumPy's broadcasting functionality. 

Broadcasting is simply a set of rules for applying binary ufuncs (e.g., addition, subtraction, multiplication, etc.) on arrays of different sizes.

### Introducing Broadcasting

```python
import numpy as np
a = np.array([0, 1, 2])
b = np.array([5, 5, 5])
print('a + b = ', a + b)
print('a + 5 =', a + 5)

c = np.ones((3, 3))
print('c:', c)
print('c + a', c + a)

d = np.arange(3)
e = np.arange(3)[:, np.newaxis]
print('d = ', d)
print('e = ', e)
print('d + e = ', e)


```
Recall that for arrays of the same size, binary operations are performed on an element-by-element basis

Broadcasting allows these types of binary operations to be performed on arrays of different sizes

for example:

add a scalar (think of it as a zero-dimensional array) to an array

Here the one-dimensional array a is stretched, or broadcast across the second dimension in order to match the shape of M.

![broadcast](../assets/images/05-broadcasting.png)

The light boxes represent the broadcasted values: again, this extra memory is not actually allocated in the course of the operation, but it can be useful conceptually to imagine that it is.

### Rules of Broadcasting

1. If the two arrays differ in their number of dimensions, the shape of the one with fewer dimensions is padded with ones on its leading (left) side.

2. If the shape of the two arrays does not match in any dimension, the array with shape equal to 1 in that dimension is stretched to match the other shape.

3. If in any dimension the sizes disagree and neither is equal to 1, an error is raised.

#### Example

```python

    # adding a two-dimensional array to a one-dimensional array:
    a = np.ones((2, 3))
    b = np.arange(3)
    print('a + b = ', a + b)

    # both arrays need to be broadcast:
    a2 = np.arange(3).reshape((3, 1))
    b2 = np.arange(3)
    print('a2 + b2 = ', a2 + b2)

    #  the two arrays are not compatible:
    a3 = np.ones((3, 2))
    b3 = np.arange(3)
    # print('a3 + b3 = ', a3 + b3)  # ValueError: operands could not be broadcast
    b4 = b3[:, np.newaxis]
    print('a3 + b4 = ', a3 + b4)
    np.logaddexp(a3, b4)  # logaddexp(a, b) function, which computes log(exp(a) + exp(b))

    # define a function $z = f(x, y)
    x = np.linspace(0, 5, 50)
    y = np.linspace(0, 5, 50)[:, np.newaxis]
    z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)
    print('z = ', z)

```
