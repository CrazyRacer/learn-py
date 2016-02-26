##IndentationError: unexpected indent  错误是python编译器是在告诉你"Hi，老兄，你的文件里格式不对了，可能是tab和空格没对齐的问题
##IndentationError: unindent does not match any outer indentation level错误表明，你使用的缩进方式不一致，有的是 tab 键缩进，有的是空格缩进，改为一致即可。


##python 的数据类型:

Numbers（数字）
String（字符串）
List（列表）
Tuple（元组）
Dictionary（字典）

##数字类型有以下几种:
int（有符号整型）
long（长整型[也可以代表八进制和十六进制]）
float（浮点型）
complex（复数）


##del可以删除对象的引用  相当于 java = null


##python 数据类型转换

int(x [,base])
将x转换为一个整数
long(x [,base] )
将x转换为一个长整数
float(x)
将x转换到一个浮点数
complex(real [,imag])
创建一个复数
str(x)
将对象 x 转换为字符串
repr(x)
将对象 x 转换为表达式字符串
eval(str)
用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)
将序列 s 转换为一个元组
list(s)
将序列 s 转换为一个列表
set(s)
转换为可变集合
dict(d)
创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)
转换为不可变集合
chr(x)
将一个整数转换为一个字符
unichr(x)
将一个整数转换为Unicode字符
ord(x)
将一个字符转换为它的整数值
hex(x)
将一个整数转换为一个十六进制字符串
oct(x)
将一个整数转换为一个八进制字符串