# day 5 Numpy

import numpy as np


def introduction():
    print('Numpy Version', np.__version__)


def array_operation():
    np.random.seed(0)  # seed for reproducibility
    x1 = np.random.randint(10, size=6)      # One-dimensional array
    x2 = np.random.randint(10, size=(3, 4))  # Two-dimensional array
    x3 = np.random.randint(10, size=(3, 4, 5))  # Three-dimensional array

    print("x3 ndim: ", x3.ndim)
    print("x3 shape:", x3.shape)
    print("x3 size: ", x3.size)
    print("dtype:", x3.dtype)
    print("itemsize:", x3.itemsize, "bytes")
    print("nbytes:", x3.nbytes, "bytes")

    print('X1', x1)
    print('x1[0]', x1[0])
    print('x1[-1]', x1[-1])
    print('x2', x2)
    print('x2[0,0]', x2[0, 0])
    print('x2[1,-1]', x2[1, -1])
    x2[0, 0] = 12
    print('x2', x2)


def array_sub():
    x = np.arange(10)
    print('x', x)
    print('x[:5]', x[:5])
    print('x[5:]', x[5:])
    print('x[3:5]', x[3:5])
    print('x[::2]', x[::2])
    print('x[1::2]', x[1::2])
    print('x[::-1]', x[::-1])
    print('x[5::-2]', x[5::-2])

    x2 = np.random.randint(10, size=(3, 4))
    print('x2', x2)
    print('x2[:2, :3]', x2[:2, :3])  # 2x3
    print('x2[:3, ::2]', x2[:3, ::2])
    print('x2[::-1, ::-1]', x2[::-1, ::-1])
    print('x2[:, 0]', x2[:, 0])  # first column of x2
    print('x2[0, :]', x2[0, :])  # first row of x2
    print(x2[0], x2[0])  # equivalent to x2[0, :]

    x2_sub = x2[:2, :2]
    print('sub, x2[0, :]', x2_sub)
    x2_sub[0, 0] = 99
    print(x2_sub)
    print('x2', x2)  # Sub arrays as no-copy views
    x2_sub_copy = x2[:2, :2].copy() # Creating copies of arrays
    print(x2_sub_copy)


def array_reshape():
    x = np.array([1, 2, 3])
    print('x', x)
    reshape1 = x.reshape(1, 3)
    reshape2 = x[np.newaxis, :]
    reshape3 = x.reshape(3, 1)
    reshape4 = x[:, np.newaxis]
    print('reshape', reshape1)
    print('newaxis', reshape2)
    print('reshape', reshape3)
    print('newaxis', reshape4)
    x[2] = 999
    print('reshape', reshape1)
    print('newaxis', reshape2)
    print('reshape', reshape3)
    print('newaxis', reshape4)


def concat_split():
    x = np.array([1, 2, 3])
    y = np.array([3, 2, 1])
    con1 = np.concatenate([x, y])
    print('concatenate([x,y])', con1)
    z = np.array([99, 99, 99])
    con2 = np.concatenate([x, y, z])
    print('concatenate([x, y, z])', con2)

    grid = np.array([[1, 2, 3],
                     [4, 5, 6]])
    con3 = np.concatenate([grid, grid])
    print('2 dims concatenate([x, y])', con3)
    con4 = np.concatenate([grid, grid], axis=1)
    print('2 dims concatenate([x, y,axis=1])', con4)

    x = np.array([9, 9, 9])
    grid = np.array([[1, 1, 1],
                     [1, 1, 1]])
    con5 = np.vstack([x, grid])
    print('mix dims vstack([x, y])', con5)
    y = np.array([[99],
                  [99]])
    con6 = np.hstack([grid, y])
    print('mix dims hstack([x, y])', con6)

    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x1, x2, x3 = np.split(x, [1, 2])
    print('split', x1, x2, x3)
    grid = np.arange(16).reshape((4, 4))
    print('2dim split', x1, x2)
    up, down = np.vsplit(grid, [2])
    print(up)
    print(down)
    left, right = np.hsplit(grid, [2])
    print(left)
    print(right)


if __name__ == '__main__':
    # introduction()
    # array_operation()
    # array_reshape()
    concat_split()


