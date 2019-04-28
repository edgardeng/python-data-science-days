## day 2 Python General Function

### 数值函数 Number

|函数|	描述|	实例|
|:----|:----|:----|
|abs(x) | 数字的绝对值 |abs(-10) 返回 10|
|ceil(x)| 返回数字的上入整数|math.ceil(4.1) 返回 5|
|exp(x) |返回e的x次幂(ex) |math.exp(1) 返回2.718281828459045|
|fabs(x) |返回数字的绝对值|math.fabs(-10) 返回10.0|
|floor(x) |返回数字的下舍整数|math.floor(4.9)返回 4|
|log(x) |如math.log(math.e) |返回1.0,math.log(100,10)返回2.0|
|log10(x)| 返回以10为基数的x的对数|math.log10(100)返回 2.0|
|max(x1, x2,…) |返回给定参数的最大值，参数可以为序列。||
|min(x1, x2,…) |返回给定参数的最小值，参数可以为序列。||
|modf(x)| 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。||
|pow(x, y)|求次方 |x**y 运算后的值。|
|round(x [,n]) |返回浮点数x的四舍五入值|给出n值，则代表舍入到小数点后的位数。|
|sqrt(x)| 返回数字x的平方根| |


__三角函数  Trigonometric __ 

|函数|	描述|
|:----|:----|
|acos(x) |x的反余弦弧度值。|
|asin(x) |x的反正弦弧度值。|
|atan(x) |x的反正切弧度值。|
|atan2(y, x) |给定的 X 及 Y 坐标值的反正切值。|
|cos(x) |x的弧度的余弦值。|
|hypot(x, y) |欧几里德范数 sqrt(xx + yy)。|
|sin(x) |x弧度的正弦值。|
|tan(x) |x弧度的正切值。|
|degrees(x) |将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0|
|radians(x) |将角度转换为弧度|

__数学常量 Math Constant__

|函数|解释|
|:----|:----|
| pi |圆周率,一般以π来表示|
| e |自然常数|

### 字符函数 String

|函数|解释|
|:----|:----|
| capitalize |将字符串的第一个字符转换为大写|
| center(width, fillchar) |返回一个指定的宽度 width 居中的字符串，fillchar 为填充的字符，默认为空格。|
| count(str, beg= 0,end=len(string))|返回 str 在 string 里面出现的次数|
| endswith(suffix, beg=0, end=len(string)) |检查字符串是否以 obj 结束|
| startswith(substr, beg=0,end=len(string))|检查字符串是否是以指定子字符串 substr 开头|
| upper()|转小写字母为大写|
| swapcase()|大写转换为小写，小写转换为大写|
| lower() | 转所有大写字符为小写.|
| isnumeric() |是否只包含数字字符|
| find(str, beg=0, end=len(string))| 检测 str 是否包含在字符串中，指定范围 beg 和 end|
| index(str, beg=0, end=len(string))|跟find()方法一样，如果str不在字符串中会报一个异常.|
| join(seq)|指定字符串作为分隔符，将 seq 中所有的元素(的字符串表示)合并为一个新的字符串|