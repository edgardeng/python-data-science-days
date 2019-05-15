## day 12 Numpy Structured Array

While often our data can be well represented by a homogeneous array of values, sometimes this is not the case. This section demonstrates the use of NumPy's structured arrays and record arrays, which provide efficient storage for compound, heterogeneous data.

### Creating Structured Arrays

Structured array data types can be specified in a number of ways. 

* the dictionary method: `np.dtype({'names':('name', 'age', 'weight'),'formats':('U10', 'i4', 'f8')})`

* use Python types or NumPy dtype: `np.dtype({'names':('name', 'age', 'weight'),'formats':((np.str_, 10), int, np.float32)})`

* list of tuples: `np.dtype([('name', 'S10'), ('age', 'i4'), ('weight', 'f8')])`

* a comma-separated string: `np.dtype('S10,i4,f8')`


The first (optional) character is ``<`` or ``>``, which means "little endian" or "big endian," respectively, and specifies the ordering convention for significant bits.

The next character specifies the type of data: characters, bytes, ints, floating points, and so on (see the table below).

The last character or characters represents the size of the object in bytes.

type list below: 

| Character        | Description           | Example                             |
| ---------        | -----------           | -------                             | 
| ``'b'``          | Byte                  | ``np.dtype('b')``                   |
| ``'i'``          | Signed integer        | ``np.dtype('i4') == np.int32``      |
| ``'u'``          | Unsigned integer      | ``np.dtype('u1') == np.uint8``      |
| ``'f'``          | Floating point        | ``np.dtype('f8') == np.int64``      |
| ``'c'``          | Complex floating point| ``np.dtype('c16') == np.complex128``|
| ``'S'``, ``'a'`` | String                | ``np.dtype('S5')``                  |
| ``'U'``          | Unicode string        | ``np.dtype('U') == np.str_``        |
| ``'V'``          | Raw data (void)       | ``np.dtype('V') == np.void``        |

### More Advanced Compound Types

It is possible to define even more advanced compound types.

For example, you can create a type where each element contains an array or matrix of values.
Here, we'll create a data type with a ``mat`` component consisting of a 3x3 floating-point matrix:

```python
tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3, 3))])
X = np.zeros(1, dtype=tp)
print(X[0])
print(X['mat'][0])
```

 NumPy ``dtype`` directly maps onto a C structure definition, so the buffer containing the array content can be accessed directly within an appropriately written C program.
If you find yourself writing a Python interface to a legacy C or Fortran library that manipulates structured data, you'll probably find structured arrays quite useful!

### RecordArrays: Structured Arrays with a Twist

NumPy also provides the ``np.recarray`` class, which is almost identical to the structured arrays just described, but with one additional feature: fields can be accessed as attributes rather than as dictionary keys.

Recall that we previously accessed the ages by writing: `data['age'] `

If we view our data as a record array instead, we can access this with slightly fewer keystrokes:

```python
data_rec = data.view(np.recarray)
data_rec.age
```

The downside is that for record arrays, there is some extra overhead involved in accessing the fields, even when using the same syntax. 

```python
%timeit data['age']
%timeit data_rec['age']
%timeit data_rec.age
```
