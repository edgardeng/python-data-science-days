import numpy as np


def compare_operate():
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


def compare_count():
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

    print('< 5 mask: ', a[a < 5])
    print('< 5 mask median:', np.median(a[a < 5]))
    more = a > 5
    even = a % 2 == 0
    print('> 5 & even mask median:', np.median(a[more & even]))


def keywords_vs_operators():
    print('bool(42) =', bool(42), 'bool(0) =', bool(0))
    print('bool(42 and 0) =', bool(42 and 0), 'bool(42 or 0) =', bool(42 or 0))
    print('bin(42) =', bin(42), 'bin(59) =', bin(59))
    print('bin(42 & 59) =', bin(42 & 59), 'bin(42 | 0) =', bin(42 | 59))

    a = np.array([1, 0, 1, 0, 1, 0], dtype=bool)
    b = np.array([1, 1, 1, 0, 1, 1], dtype=bool)
    print('A | B = ', a | b)
    # print('A or B = ', a or b) # ValueError: The truth value of an array with more than one element is ambiguous
    x = np.arange(10)
    print('(x > 4) & (x < 8)', (x > 4) & (x < 8))
    # print('(x > 4) and (x < 8)', (x > 4) and (x < 8)) # ValueError:


if __name__ == '__main__':
    print('Numpy Version', np.__version__)
    # compare_operate()
    # compare_count()
    keywords_vs_operators()
