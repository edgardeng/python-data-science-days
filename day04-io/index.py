# day 4 Python I/O


def write_file():
    try:
        # /Users/documents/test.txt
        f = open('test.txt', 'w')
        f.write('Hello, 1 \r\n One!\r\nTwo\r\nThree')
    finally:
        if f:
            f.close()
    with open('test.txt', 'a') as f2:
        f2.write('\r\nHello, 2 \r\n One!\r\nTwo\r\nThree')


def read_file():
    try:
        f = open('test.txt', 'r')
        print(f.read())
    finally:
        if f:
            f.close()
    with open('test.txt', 'r') as f2:
        print(f2.read())
    with open('test.txt', 'r') as f2:
        print('---- lines ------')
        for line in f2.readlines():
            print(line.strip())  # 把末尾的'\n'删掉


from io import StringIO, BytesIO


def stream_operate():
    f = StringIO()
    f.write('hello')
    f.write(' ')
    f.write('world!')
    print('write StringIO: ', f.getvalue())

    f2 = StringIO('Hello!\nHi!\nGoodbye!')
    while True:
        s = f2.readline()
        if s == '':
            break
        print('StringIO readline:', s.strip())

    f3 = BytesIO()
    f3.write('中文'.encode('utf-8'))
    print('write BytesIO:', f3.getvalue())

    f4 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
    print('read BytesIO:', f4.read())


import os


def file_operate():
    print('OS name:', os.name)  # 操作系统类型
    print('OS uname:', os.uname())  # 获取详细的系统信息
    print('OS environ:', os.environ)  # 环境变量
    print('OS environ Value:', os.environ.get('PATH'))  # 环境变量
    print('OS getcwd:', os.getcwd())  # 工作目录路径
    print('OS abspath file:', os.path.abspath(__file__))  # 当前文件
    print('OS realpath file:', os.path.realpath(__file__))  # 当前文件
    print('OS abspath:', os.path.abspath('.'))  # 查看当前目录的绝对路径:
    print('OS basename:', os.path.basename('.'))  # 返回一个目录的基名
    print('OS basename:', os.path.dirname("/etc/sysconfig/selinux"))  # 返回一个目录的目录名
    print('OS exists:', os.path.exists("./test.txt"))  # 是否存在
    print('OS exists:', os.path.exists("/Users/Shared/Documents/testdir"))  # 是否存在
    print('OS path join:', os.path.join('/Users/Documents', 'testdir'))
    os.mkdir('/Users/Shared/Documents/testdir')  # 然后创建一个目录:
    print('OS exists:', os.path.exists("/Users/Shared/Documents/testdir"))  # 是否存在
    os.rmdir('/Users/Shared/Documents/testdir')  # 删掉一个目录:
    os.path.split('/Users/Shared/Documents/test.txt')
    os.path.splitext('/Users/Shared/Documents/test.txt')
    os.rename('test.txt', 'test.py') # 重命名
    os.remove('test.py') # 删掉文件:
    list_1 = [x for x in os.listdir('.') if os.path.isdir(x)] # 列出当前目录下的所有目录
    for l in list_1:
        print(l)
    list_2 = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']  # 列出Py文件
    for l in list_2:
        print(l)


import pickle


def pickle_operate():
    d = dict(name='Bob', age=20, score=88)
    pickle.dumps(d)
    print('pickle.dumps:', d)
    f = open('dump.txt', 'wb')
    pickle.dump(d, f)
    f.close()
    f2 = open('dump.txt', 'rb')
    print('pickle.load:',  pickle.load(f2))
    f2.close()


import json


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


def json_operate():
    d = dict(name='Bob', age=20, score=88)
    json.dumps(d)
    print('json.dumps:', d)
    json_str = '{"age": 20, "score": 88, "name": "Bob"}'
    print('json.loads:', json.loads(json_str))

    s = Student('Bob', 20, 88)
    # print('Class json.dumps:', json.dumps(s))
    print('Class json.dumps:', json.dumps(s, default=student2dict))
    print('Class json.dumps:', json.dumps(s, default=lambda obj: obj.__dict__))

    json_str = '{"age": 0, "score": 80, "name": "Abby"}'
    print('json.loads:', json.loads(json_str))
    print('Class json.loads:', json.loads(json_str, object_hook=dict2student))


if __name__ == '__main__':
    # write_file()
    # read_file()
    # stream_operate()
    # file_operate()
    # pickle_operate()
    json_operate()

