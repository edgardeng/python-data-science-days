## day 3 Python List & Array

### List
> 序列是Python中最基本的数据结构。

```python
# 访问值
list = [1, 2, 3, 4, 5, 6, 7 ]
print "list[0]: ", list[0]
print "list[1:5]: ", list[1:5]

# 使用 append() 添加元素
list.append(8)
print list
# 删除元素
del list[2]
print list
```

### Array
> 计算机为数组分配一段连续的内存，从而支持对数组随机访问；
由于项的地址在编号上是连续的，数组某一项的地址可以通过将两个值相加得出，即将数组的基本地址和项的偏移地址相加。
数组的基本地址就是数组的第一项的机器地址。一个项的偏移地址就等于它的索引乘以数组的一个项所需要的内存单元数目的一个常量表示（在python中，这个值总是1）

```python
import array
#array模块是一种高效的数组存储类型。它和list相似，但是所有的数组成员必须是同一种类型，在创建数组的时候，就确定了数组的类型

#array.array(typecode,[initializer]) --typecode:元素类型代码；initializer:初始化器，若数组为空，则省略初始化器
arr = array.array('i',[0,1,1,3])
print(arr)

#array.typecodes --模块属性
print('\n输出一条 包含所有可用类型代码的字符串：')
print(array.typecodes) #注意调用者是模块名，不是某个对象

#array.typecode -- 对象属性
print('\n 输出 用于创建数组的类型代码字符：')
print(arr.typecode)

#array.itemsize --对象属性
print('\n输出 数组的元素个数：')
print(arr.itemsize)

#array.append(x) --对象方法
print('\n将一个新值附加到数组的末尾：')
arr.append(4)
print(arr)

#array.buffer_info() -- 对象方法
print('\n获取数组在存储器中的地址、元素的个数，以元组形式（地址、长度）返回：')
print(arr.buffer_info())

#array.count(x) -- 对象方法
print('\n获取元素1在数组中出现的次数：')
print(arr.count(1))

#array.extend(iterable) -- 对象方法：将可迭代对象的袁旭序列附加到数组的末尾，合并两个序列
print('\n将可迭代对象的元素序列附加到数据的末尾，合并两个序列：')
#注意：附加元素数值类型必须与调用对象的元素的数值类型一致
_list = [5,6,7]
arr.extend(_list)
print(arr)

#array.fromlist(list) --对象方法：将列表中的元素追加到数组后面，相当于for x in list:a.append(x)
print('\n将列表中的元素追加到数组后面，相当于for x in list:a.append(x):')
arr.fromlist(_list)
print(arr)

#array.index(x) --对象方法：返回数组中x的最小下标
print('\n返回数组中1的最小下标：')
print(arr.index(1))

#array.insert(1) --对象方法：在下表i（负值表示倒数）之前插入值x
print('\n在下表1（负值表示倒数）之前插入值0：')
arr.insert(1,0)
print(arr)

#array.pop(i) --对象方法：删除索引为i的项，并返回它
print('\n删除索引为4的项，并返回它:')
print(arr.pop(4))
print(arr)

#array.remove(x) --对象方法：删除第一次出现的元素x
print('\n删除第一次出现的元素5：')
arr.remove(5)
print(arr)

#array.reverse() --对象方法：反转数组中的元素值
print('\n将数组arr中元素的顺序反转：')
arr.reverse()
print(arr)

#array.tolist()：将数组转换为具有相同元素的列表（list）
print('\n将数组arr转换为已给具有相同元素的列表：')
li = arr.tolist()
print(li)
```
