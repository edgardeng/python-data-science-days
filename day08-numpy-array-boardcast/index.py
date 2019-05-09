import numpy as np


def broadcast_operate():
    a = np.array([0, 1, 2])
    b = np.array([5, 5, 5])
    print('a:', a)
    print('b:', b)
    print('a + b = ', a + b)
    print('a + 5 =', a + 5)

    c = np.ones((3, 3))
    print('c:', c)
    print('c + a', c + a)

    d = np.arange(3)
    e = np.arange(3)[:, np.newaxis]
    print('d = ', d)
    print('e = ', e)
    print('d + e = ', d + e)


def broadcast_operate_example():
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


if __name__ == '__main__':
    print('Numpy Version', np.__version__)
    # broadcast_operate()
    broadcast_operate_example()
