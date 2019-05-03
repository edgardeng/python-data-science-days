## day 6 Numpy Array Universal Function

Computation on NumPy arrays can be very fast, or it can be very slow.
The key to making it fast is to use *vectorized* operations, generally implemented through NumPy's *universal functions* (ufuncs).

This section motivates the need for NumPy's ufuncs, which can be used to make repeated calculations on array elements much more efficient.

```python
import numpy as np
import time
from timeit import timeit
np.random.seed(0)

def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output

# time loop
value1 = np.random.randint(1, 10, size=5)
t1 = timeit('compute_reciprocals(value1)', 'from __main__ import compute_reciprocals, value1', number=1)
print('timeit', t1)

value2 = np.random.randint(1, 100, size=1000000)
t2 = timeit('compute_reciprocals(value2)', 'from __main__ import compute_reciprocals, value2', number=1)
print('timeit', t2)

t3 = timeit('1.0 / value2', 'from __main__ import value2', number=1)
print('timeit', t3)

```

### Exploring NumPy's UFuncs

#### Array arithmetic

```python
    x = np.arange(4)
    print("x     =", x)
    print("x + 5 =", x + 5)
    print("x - 5 =", x - 5)
    print("x * 2 =", x * 2)
    print("x / 2 =", x / 2)
    print("x // 2 =", x // 2)
    print("-x     = ", -x)
    print("x ** 2 = ", x ** 2)
    print("x % 2  = ", x % 2)
    print('-(0.5*x + 1) ** 2', -(0.5*x + 1) ** 2)
    print('add', np.add(x, 2))
    
```

Each of these arithmetic operations are simply convenient wrappers around specific functions built into NumPy; for example, the + operator is a wrapper for the add function:


|Operator	|Equivalent ufunc|	Description|
|:----|:----|:----|
|+	|np.add	        |Addition (e.g., 1 + 1 = 2)|
|-	|np.subtract	|Subtraction (e.g., 3 - 2 = 1)|
|-	|np.negative	|Unary negation (e.g., -2)|
|*	|np.multiply	|Multiplication (e.g., 2 * 3 = 6)|
|/	|np.divide	    |Division (e.g., 3 / 2 = 1.5)|
|//	|np.floor_divide|	Floor division (e.g., 3 // 2 = 1)|
|**	|np.power	    |Exponentiation (e.g., 2 ** 3 = 8)|
|%	|np.mod	        |Modulus/remainder (e.g., 9 % 4 = 1)|

#### Absolute value

```python
    x = np.arange(4)
    print("x     =", x)
    print("x + 5 =", x + 5)
    print("x - 5 =", x - 5)
    print("x * 2 =", x * 2)
    print("x / 2 =", x / 2)
    print("x // 2 =", x // 2)
    print("-x     = ", -x)
    print("x ** 2 = ", x ** 2)
    print("x % 2  = ", x % 2)
    print('-(0.5*x + 1) ** 2', -(0.5*x + 1) ** 2)
    print('add', np.add(x, 2))

    x = np.array([-2, -1, 0, 1, 2])
    print('x=', x)
    print('abs(x)=', abs(x))
    print('np.absolute(x) = ', np.absolute(x))
    print('np.abs(x) = ', np.abs(x))
    x = np.array([3 - 4j, 4 - 3j, 2 + 0j, 0 + 1j])
    print('x=', x)
    print('np.abs(x) = ', np.abs(x))

```

#### Trigonometric functions

```python
    theta = np.linspace(0, np.pi, 3)
    print("theta      = ", theta)
    print("sin(theta) = ", np.sin(theta))
    print("cos(theta) = ", np.cos(theta))
    print("tan(theta) = ", np.tan(theta))
    x = [-1, 0, 1]
    print("x         = ", x)
    print("arcsin(x) = ", np.arcsin(x))
    print("arccos(x) = ", np.arccos(x))
    print("arctan(x) = ", np.arctan(x)) 
```

#### Exponents and logarithms

NumPy has many more ufuncs available, including hyperbolic trig functions, bitwise arithmetic, comparison operators, conversions from radians to degrees, rounding and remainders, and much more.

```python
    x = [1, 2, 3]
    print("x     =", x)
    print("e^x   =", np.exp(x))
    print("2^x   =", np.exp2(x))
    print("3^x   =", np.power(3, x))

    x = [1, 2, 4, 10]
    print("x        =", x)
    print("ln(x)    =", np.log(x))
    print("log2(x)  =", np.log2(x))
    print("log10(x) =", np.log10(x))

    x = [0, 0.001, 0.01, 0.1]
    print("exp(x) - 1 =", np.expm1(x))
    print("log(1 + x) =", np.log1p(x))
    
```

#### Specialized ufuncs
> If you want to compute some obscure mathematical function on your data, chances are it is implemented in ``scipy.special``.

```python
    x = [1, 5, 10]
    print("gamma(x)     =", special.gamma(x))
    print("ln|gamma(x)| =", special.gammaln(x))
    print("beta(x, 2)   =", special.beta(x, 2))
    # Error function (integral of Gaussian)
    x = np.array([0, 0.3, 0.7, 1.0])
    print("erf(x)  =", special.erf(x))
    print("erfc(x) =", special.erfc(x))
    print("erfinv(x) =", special.erfinv(x))
    
```

### Advanced Ufunc Features

#### Specifying output

```python
    x = np.arange(5)
    y = np.empty(5)
    np.multiply(x, 10, out=y)
    print(y)

    y = np.zeros(10)
    np.power(2, x, out=y[::2])
    print(y)

```

####  Aggregates

```python
    x = np.arange(1, 6)
    sum = np.add.reduce(x)
    mul = np.multiply.reduce(x)
    
    sum2 = np.add.accumulate(x)
    mul2 = np.multiply.accumulate(x)
    
```

#### Outer products
```python
x = np.arange(1, 6)
out = np.multiply.outer(x, x)
```