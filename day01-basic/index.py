def arithmetic(a, b):
    print('a+b =', a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a % b)
    print(a ** b)
    print(a // b)


def compare(a, b):
    print('compare: ', a, ', ', b)
    print('a == b :', a == b)
    print('a != b :', a != b)
    print('a > b :', a > b)
    print('a < b :', a < b)
    print('a <= b :', a <= b)
    print('a >= b :', a >= b)


def logic(a, b):
    print('logic: ', a, ', ', b)
    print('a and b :', a and b)
    print('a or b :', a or b)
    print('not a:', not a)


def member(a, b):
    print('member: ', a, ', ', b)
    print('a in b :', a in b)
    print('a not in b :', a not in b)
    print('a is b:', a is b)
    print('a is not b:', a is not b)


def bit(a, b):
    print('bit: ', a, ', ', b)
    print('a & b :', a & b)
    print('a | b :', a | b)
    print('a ^ b:', a ^ b)
    print('~a:', ~a)
    print('a << 2:', a << 2)
    print('a >> 2:', a >> 2)


if __name__ == '__main__':
    # arithmetic(10, 3)
    # arithmetic(10.0, 3.0)
    # compare(10, 3)
    # compare(3.00, 3)
    # logic(True, False)
    # logic(20, 10)
    member(1, [1, 2, 3, 4])
    bit(60, 13)