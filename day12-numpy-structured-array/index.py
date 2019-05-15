import numpy as np
import time


def advanced_array():
    tp = np.dtype([('id', 'i8'), ('mat', 'f8', (3, 3))])
    X = np.zeros(1, dtype=tp)
    print(X[0])
    print(X['mat'][0])


def structure_array():
    name = ['Alice', 'Bob', 'Cathy', 'Doug']
    age = [25, 45, 37, 19]
    weight = [55.0, 85.5, 68.0, 61.5]
    # Use a compound data type for structured arrays
    data = np.zeros(4, dtype={'names': ('name', 'age', 'weight'), 'formats': ('U10', 'i4', 'f8')})
    print(data.dtype)
    data['name'] = name
    data['age'] = age
    data['weight'] = weight
    print(data)
    print('data[\'name\']', data['name'])
    print('data[0]', data[0])
    print('data[-1][\'name\']', data[-1]['name'])
    print('data[data[\'age\'] < 30][\'name\']', data[data['age'] < 30]['name'])

    data_rec = data.view(np.recarray)
    print('data_rec.age', data_rec.age)


if __name__ == '__main__':
    print('Numpy Version:', np.__version__)
    structure_array()
    advanced_array()






