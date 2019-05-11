import numpy as np
import time


def fancy_index():
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


def combine_index():
    x = np.arange(12).reshape((3, 4))
    print('x = ', x)
    print('x[2, [2, 0, 1]] = ', x[2, [2, 0, 1]])
    print('x[1:, [2, 0, 1]] = ', x[1:, [2, 0, 1]])
    mask = np.array([1, 0, 1, 0], dtype=bool)
    row = np.array([0, 1, 2])
    print('x[row[:, np.newaxis], mask]', x[row[:, np.newaxis], mask])


def select_random():
    mean = [0, 0]
    cov = [[1, 2], [2, 5]]
    x = np.random.multivariate_normal(mean, cov, 100)
    print('x.shape', x.shape)
    indices = np.random.choice(x.shape[0], 20, replace=False)
    print('indices = ', indices)
    print(x[indices].shape)


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


def binning_data():
    x = np.random.randn(50)
    # compute a histogram by hand
    bins = np.linspace(-5, 5, 20)
    counts = np.zeros_like(bins)
    i = np.searchsorted(bins, x) # Find indices where elements should be inserted to maintain order
    np.add.at(counts, i, 1)

    y = np.random.randn(1000000)
    t1 = time.time()
    counts, edges = np.histogram(y, bins)
    print('counts:', counts, edges)
    t2 = time.time()
    np.add.at(counts, np.searchsorted(bins, x), 1)
    t3 = time.time()
    print("NumPy routine:", t2 - t1)
    print("Custom routine:", t3 - t2)


if __name__ == '__main__':
    print('Numpy Version:', np.__version__)
    # fancy_index()
    # combine_index()
    # select_random()
    # modify_value()
    binning_data()
