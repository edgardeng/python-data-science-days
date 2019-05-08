# day 6 Numpy Array Function
import numpy as np
from math import *


def aggregate_operate():
    L = np.random.random(50)
    print('Array:', L, '\r\n')
    print('python sum:', sum(L))
    print('numpy sum:', np.sum(L))
    print('python min:', min(L))
    print('numpy min:', np.min(L))
    print('python max:', max(L))
    print('numpy max:', np.max(L))
    print('min:', L.min(), 'max:', L.max(), 'sum:', L.sum())


def multi_dimension_aggregate():
    M = np.random.random((4, 5))
    print('Array:', M, '\r\n')
    print('min:', M.min(), 'max:', M.max(), 'sum:', M.sum())
    print('min(axis=0):', M.min(axis=0))
    print('max(axis=1):', M.max(axis=1))


def other_aggregate_operate():
    l = np.random.randint(100, size=20)
    print('Array:', l, '\r\n')
    print("Mean :       ", l.mean())
    print("Standard deviation:", l.std())
    print("Minimum :    ", l.min())
    print("Maximum :    ", l.max())
    print("25th percentile:   ", np.percentile(l, 25))
    print("Median:            ", np.median(l))
    print("75th percentile:   ", np.percentile(l, 75))
    b = l > 50
    print("has bigger :", b.any())
    print("all bigger :", b.all())


if __name__ == '__main__':
    print('Numpy Version', np.__version__)
    # aggregate_operate()
    # multi_dimension_aggregate()
    other_aggregate_operate()
