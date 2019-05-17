## Day 13 Matplotlib Introduction

Matplotlib is a Python 2D plotting library which produces publication-quality figures in a variety of hardcopy formats and interactive environments across platforms. 

### Basic

#### Pyplot

Pyplot provides the state-machine interface to the underlying object-oriented plotting library. 

```python
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()
```

#### Figure

>The figure keeps track of all the child Axes, a smattering of 'special' artists (titles, figure legends, etc), and the canvas.

![image](../assets/images/13-plot_figure.webp)

The easiest way to create a new figure:

```python
import matplotlib.pyplot as plt
fig = plt.figure()  # an empty figure with no axes
fig.suptitle('No axes on this figure')  # Add a title so we know which it is
fig, ax_lst = plt.subplots(2, 2) 
```

Matplotlib allows you to pass categorical variables directly to many plotting functions.

```python
names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(1, figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()
```

You can create multiple figures by using multiple figure() calls with an increasing figure number. Of course, each figure can contain as many axes and subplots as your heart desires:

```python
import matplotlib.pyplot as plt
plt.figure(1)                # 第一张图
plt.subplot(211)             # 第一张图中的第一张子图
plt.plot([1,2,3])
plt.subplot(212)             # 第一张图中的第二张子图
plt.plot([4,5,6])

plt.figure(2)                # 第二张图
plt.plot([4,5,6])            # 默认创建子图subplot(111)

plt.figure(1)                # 切换到figure 1 ; 子图subplot(212)仍旧是当前图
plt.subplot(211)             # 令子图subplot(211)成为figure1的当前图
plt.title('Easy as 1,2,3')   # 添加subplot 211 的标题
```

#### Formatting the style of your plot

there is an optional third argument which is the format string that indicates the color and line type of the plot

```python
    plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
    plt.axis([0, 6, 0, 20])
    plt.show()
```
The example below illustrates a plotting several lines with different format styles in one command using arrays.

```python
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
plt.show()
```

#### Plotting with keyword strings

Matplotlib allows you provide such an object with the data keyword argument. If provided, then you may generate plots with the strings corresponding to these variables.
```python
data = {'a': np.arange(50),
        'c': np.random.randint(0, 50, 50),
        'd': np.random.randn(50)}
data['b'] = data['a'] + 10 * np.random.randn(50)
data['d'] = np.abs(data['d']) * 100

plt.scatter('a', 'b', c='c', s='d', data=data)
plt.xlabel('entry a')
plt.ylabel('entry b')
plt.show()
```

#### Plotting with categorical variables

```python
    names = ['group_a', 'group_b', 'group_c']
    values = [1, 10, 100]

    plt.figure(1, figsize=(9, 3))

    plt.subplot(131)
    plt.bar(names, values)
    plt.subplot(132)
    plt.scatter(names, values)
    plt.subplot(133)
    plt.plot(names, values)
    plt.suptitle('Categorical Plotting')
    plt.show()
```

#### text

The text() command can be used to add text in an arbitrary location, and the xlabel(), ylabel() and title() are used to add text in the indicated locations 

```python
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=1, facecolor='g', alpha=0.75)

plt.xlabel('Smarts')
# t = plt.xlabel('my data', fontsize=14, color='red')
plt.ylabel('Probability')
plt.title('Histogram of IQ')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()
```

A common use for text is to annotate some feature of the plot, and the __annotate()__ method provides helper functionality to make annotations easy
 
```python
ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.05))

plt.ylim(-2, 2)
plt.show()
```

#### Logarithmic and other nonlinear axes

matplotlib.pyplot supports not only linear axis scales, but also logarithmic and logit scales.

```python
from matplotlib.ticker import NullFormatter  # useful for `logit` scale

# Fixing random state for reproducibility
np.random.seed(19680801)

# make up some data in the interval ]0, 1[
y = np.random.normal(loc=0.5, scale=0.4, size=1000)
y = y[(y > 0) & (y < 1)]
y.sort()
x = np.arange(len(y))

# plot with various axes scales
plt.figure(1)

# linear
plt.subplot(221)
plt.plot(x, y)
plt.yscale('linear')
plt.title('linear')
plt.grid(True)

# log
plt.subplot(222)
plt.plot(x, y)
plt.yscale('log')
plt.title('log')
plt.grid(True)

# symmetric log
plt.subplot(223)
plt.plot(x, y - y.mean())
plt.yscale('symlog', linthreshy=0.01)
plt.title('symlog')
plt.grid(True)

# logit
plt.subplot(224)
plt.plot(x, y)
plt.yscale('logit')
plt.title('logit')
plt.grid(True)
# Format the minor tick labels of the y-axis into empty strings with
# `NullFormatter`, to avoid cumbering the axis with too many labels.
plt.gca().yaxis.set_minor_formatter(NullFormatter())
# Adjust the subplot layout, because the logit one may take more space
# than usual, due to y-tick labels like "1 - 10^{-3}"
plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25, wspace=0.35)
plt.show()
``` 

### Params

#### Zh-cn

``` python
plt.rcParams['font.sas-serig']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
```

配置文件包括以下配置项：

axex: 设置坐标轴边界和表面的颜色、坐标刻度值大小和网格的显示
backend: 设置目标暑促TkAgg和GTKAgg
figure: 控制dpi、边界颜色、图形大小、和子区( subplot)设置
font: 字体集（font family）、字体大小和样式设置
grid: 设置网格颜色和线性
legend: 设置图例和其中的文本的显示
line: 设置线条（颜色、线型、宽度等）和标记
patch: 是填充2D空间的图形对象，如多边形和圆。控制线宽、颜色和抗锯齿设置等。
savefig: 可以对保存的图形进行单独设置。例如，设置渲染的文件的背景为白色。
verbose: 设置matplotlib在执行期间信息输出，如silent、helpful、debug和debug-annoying。
xticks和yticks: 为x,y轴的主刻度和次刻度设置颜色、大小、方向，以及标签大小。

#### Colors

The following color abbreviations are supported:

|character	|color|
|:----|:----|
|'b'	|blue|
|'g'	|green|
|'r'	|red|
|'c'	|cyan|
|'m'	|magenta|
|'y'	|yellow|
|'k'	|black|
|'w'	|white|

If the color is the only part of the format string, you can additionally use any matplotlib.colors spec, e.g. full names ('green') or hex strings ('#008000').

#### Markers

|character	|description|
|:----|:----|
|'.'	|point marker |
|','	|pixel marker |
|'o'	|circle marker |
|'v'	|triangle_down marker |
|'^'	|triangle_up marker |
|'<'	|triangle_left marker |
|'>'	|triangle_right marker |
|'1'	|tri_down marker |
|'2'	|tri_up marker |
|'3'	|tri_left marker |
|'4'	|tri_right marker |
|'s'	|square marker |
|'p'	|pentagon marker |
|'*'	|star marker |
|'h'	|hexagon1 marker |
|'H'	|hexagon2 marker |
|'+'	|plus marker |
|'x'	|x marker |
|'D'	|diamond marker |
|'d'	|thin_diamond marker |
|'&#124;'	|vline marker |
|'_'	|hline marker |

#### Line Styles

|character	|description|
|:----|:----|
|'-'|	solid line style |
|'--'|	dashed line style |
|'-.'|	dash-dot line style|
|':'|	dotted line style|


### Reference

* [matplotlib tutorialsI](https://matplotlib.org/tutorials/index.html)

* [matplotlib API](https://matplotlib.org/api/)