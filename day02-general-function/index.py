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


def trigonometric(x, y):
    print('trigonometric, x: ', x, ', y: ', y)
    print('acos(x)', acos(x))
    print('asin(x)', asin(x))
    print('atan(x)', atan(x))
    print('atan2(y, x)', atan2(y, x))
    print('cos(x)', cos(x))
    print('hypot(x, y)', hypot(x, y))
    print('sin(x)', sin(x))
    print('tan(x)', tan(x))
    print('degrees(x)', degrees(x))
    print('radians(x)', radians(x))


def string_operate(x, y):
    print("x: %s, length: %d , y: %s " % (x, len(x), y))
    xlist = ''
    for i in x:
        xlist += i + ','
    print('i in x', xlist)
    print('y in x', y in x)
    print('x[1:3]', x[1:3])
    print('x.split( )', x.split( ))
    print('x.split(y, 1)', x.split(y, 1))
    print('x.count(y)', x.count(y))
    print('x.startswith(y)', x.startswith(y))
    print('x.endswith(y)', x.endswith(y))
    print('x.upper()', x.upper())
    print('x.lower()', x.lower())
    print('x.swapcase()', x.swapcase())
    print('x.isnumeric()', x.isnumeric())
    print('x.find(y)', x.find(y))
    print('x.index(y)', x.index(y))
    seq = ("1", "2", "3")  # 字符串序列
    print('y.join(y,x)', y.join(seq))


if __name__ == '__main__':
    # number_operate(5.1, 1.2)
    # trigonometric(pi / 4, pi/4)
    string_operate('dcbahijk1Aabcdkjih', 'a')