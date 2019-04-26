from math import *


def number_operate(x, y):
    print('x: ', x, ', y: ', y)
    print('abs(x)', abs(x))
    print('ceil(x)', ceil(x))
    print('exp(x)', exp(x))
    print('fabs(x)', fabs(x))
    print('floor(x)', floor(x))
    print('log(x)', log(x))
    print('log10(x)', log10(x))
    print('max(x,y)', max(x, y))
    print('min(x,y)', min(x, y))
    print('modf(x)', modf(x))
    print('pow(x,y)', pow(x, y))
    print('round(x,y)', round(x, ceil(y)))
    print('sqrt(x)', sqrt(x))


if __name__ == '__main__':
    number_operate(5.1, 1.2)