## day 4 Python I/O

### 文件 File

#### 读文件 Read

以读文件的模式打开一个文件对象，使用Python内置的`open()`函数，传入文件名和标示符：

```python
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
        
        
```

如果文件不存在，就会抛出一个IOError的错误

如果文件打开成功，接下来，调用read()方法可以一次读取文件的全部内容，Python把内容读到内存，用一个str对象表示：

调用close()方法关闭文件。


使用with语句，自动帮我们调用close()方法：
```python
with open('/path/to/file', 'r') as f:
    print(f.read())
```
> 这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。


调用read()会一次性读取文件的全部内容，如果文件很大，内存就爆了

调用read(size)方法，每次最多读取size个字节的内容。

调用readline()可以每次读取一行内容

调用readlines()一次读取所有内容并按行返回list。

```python
for line in f.readlines():
    print(line.strip()) # 把末尾的'\n'删掉
```

#### file-like Object

open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
除了file外，还可以是内存的字节流，网络流，自定义流等等。
file-like Object不要求从特定类继承，只要写个read()方法就行。
StringIO就是在内存中创建的file-like Object，常用作临时缓冲。

#### 二进制文件
前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

```python
f = open('/Users/michael/test.jpg', 'rb')
f.read() # b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00...' # 十六进制表示的字节
```

#### 字符编码

要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：

```python
f = open('/Users/michael/test.txt', 'r', encoding='gbk')
f.read()

f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')
# 遇到UnicodeDecodeError，一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
```


### 写文件 Write

调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：

```python
 f = open('/Users/michael/test.txt', 'w')
 f.write('Hello, world!')
 f.close()
 
 with open('/Users/michael/test.txt', 'w') as f:
    f.write('Hello, world!') 
```

要写入特定编码的文本文件，请给open()函数传入encoding参数，将字符串自动转换成指定编码。

'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）

'a'以追加（append）模式, 写入追加到文件末尾

### StringIO

使用StringIO, 在内存中写str


```python
from io import StringIO
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

```


读取StringIO
```python
from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
    break
    print(s.strip())

```

### BytesIO
> 操作二进制数据，就需要使用BytesIO

```python
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())

f2 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f2.read()
```

### 操作文件和目录 OS

使用os模块的基本功能
```python
import os
print(os.name)  # 操作系统类型
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
print(os.uname())  # 获取详细的系统信息

# 环境变量
print(os.environ)
# 获取某个环境变量的值
os.environ.get('PATH')
os.environ.get('x', 'default')

```

操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中

```python
# 查看当前目录的绝对路径:
os.path.abspath('.')

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
os.path.join('/Users/Documents', 'testdir')
# 拆分路径
os.path.split('/Users/michael/testdir/file.txt')
# 得到文件扩展名
os.path.splitext('/path/to/file.txt')

#这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
# 然后创建一个目录:
os.mkdir('/Users/michael/testdir')
# 删掉一个目录:
os.rmdir('/Users/michael/testdir')
# 对文件重命名
os.rename('test.txt', 'test.py')
# 删掉文件:
os.remove('test.py')
```

复制文件的函数在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。

理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。

shutil模块提供了copyfile()的函数，在shutil模块中可以找到很多实用函数，可以看做是os模块的补充。

如何利用Python的特性来过滤文件

```python
# 列出当前目录下的所有目录
[x for x in os.listdir('.') if os.path.isdir(x)]

# 列出所有的.py文件
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
```

把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
在Linux/Unix/Mac下，os.path.join()返回这样的字符串：part-1/part-2
而Windows下会返回这样的字符串：part-1\part-2

拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：


### 序列化

> 把变量从内存中变成可存储或传输的过程称之为序列化. 在Python中叫pickling，在其他语言中也被称之为serialization，marshalling，flattening等等。

序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。

把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。

```
import pickle
d = dict(name='Bob', age=20, score=88)
pickle.dumps(d) # dumps()方法把任意对象序列化成一个bytes

f = open('dump.txt', 'wb')
pickle.dump(d, f) # dump()直接把对象序列化后写入一个file-like Object：
f.close()

f2 = open('dump.txt', 'rb')
d2 = pickle.load(f2) # load()方法从一个file-like Object中直接反序列化出对象
f2.close()
```

#### JSON

> JSON是一种把对象序列化的标准格式，可以直接在Web页面中读取

```python
import json
d = dict(name='Bob', age=20, score=88)
json.dumps(d) # dumps()方法返回一个str，内容就是标准的JSON
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
json.loads(json_str)  # 把JSON的字符串反序列化

```


JSON反序列化为对象
```python
import json

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

s = Student('Bob', 20, 88)
print(json.dumps(s))
# 遇到TypeError， 是Student对象不是一个可序列化为JSON的对象。

def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
    
print(json.dumps(s, default=student2dict)) 
# Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON    

```

[dumps()方法的参数列表](https://docs.python.org/3/library/json.html#json.dumps)

任意class的实例变为dict： ` print(json.dumps(s, default=lambda obj: obj.__dict__)) `

因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。

把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，传入的object_hook函数负责把dict转换为Student实例：

```python
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student)) # 反序列化的Student实例对象
```