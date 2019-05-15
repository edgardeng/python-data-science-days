import numpy as np
import time


def selection_sort(x):
    for i in range(len(x)):
        swap = i + np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x


def k_near():
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


def fast_sort():
    a = np.array([1, 3, 2, 7, 10, 5, 9, 8, 6, 4])
    print('a = ', a)
    # a.sort()
    # print('after a.sort(): ', a)
    i = np.argsort(a)
    print('after argsort(a) ', a)
    print('indice : ', i)
    print('a[i] = ', a[i])

    x = np.random.randint(0, 10, (4, 6))
    print('x = ', x)
    print('np.sort(x, axis=0) ', np.sort(x, axis=0))
    print('np.sort(x, axis=1)', np.sort(x, axis=1)) # sort each column of X
    print('after x = ', x)


def part_sort():
    x = np.array([7, 2, 3, 8, 6, 5, 4, 0, 9, 10])
    print('np.partition(x, 3):', np.partition(x, 3))
    print('np.partition(x, 5):', np.partition(x, 5))
    print('x = ', x)
    y = np.random.randint(0, 10, (5, 5))
    print('np.partition(y, 2, axis=0)', np.partition(y, 2, axis=0))
    print('np.partition(y, 2, axis=1)', np.partition(y, 2, axis=1))
    print('y =', y)


def bogo_sort(x):
    while np.any(x[:-1] > x[1:]):
        np.random.shuffle(x)
    return x


if __name__ == '__main__':
    print('Numpy Version:', np.__version__)
    # fast_sort()
    # part_sort()
    k_near()





