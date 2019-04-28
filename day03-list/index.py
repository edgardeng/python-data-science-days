def list_operate():
    L = list(range(10))
    print('L:', L)
    even = [x for x in L if x % 2 == 0]
    print('even:', even)
    print('type(L):', type(L))
    print('type(L[0]):', type(L[0]))
    L2 = [str(c) for c in L]
    print('L2:', L2)
    L3 = [True, '2', 3.0, 4]
    L4 = [type(item) for item in L3]
    print('L4:', L4)


import array


def array_operate():
    arr = array.array('i',[0,1,1,3])
    print(arr)
    print('array.typecodes', array.typecodes) # 注意调用者是模块名，不是某个对象
    print('arr.typecodes', arr.typecode) #array.typecode -- 对象属性
    print('arr.itemsize', arr.itemsize)
    arr.append(4)
    print('arr.append', arr)
    print('arr.buffer_info', arr.buffer_info())
    print('arr.count(1)', arr.count(1))
    _list = [5,6,7]
    arr.extend(_list)
    print('arr.extend', arr)
    arr.fromlist(_list)
    print('arr.fromlist', arr)
    print('arr.index', arr.index(1))
    arr.insert(1,0)
    print('arr.insert', arr)
    print(arr.pop(4))
    print('arr.pop', arr)
    arr.remove(5)
    print('arr.remove', arr)
    arr.reverse()
    print('arr.reverse', arr)
    li = arr.tolist()
    print('arr.tolist', li)


if __name__ == '__main__':
    array_operate()
    list_operate()