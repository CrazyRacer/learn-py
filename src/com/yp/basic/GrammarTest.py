# -*- coding: UTF-8 -*-
'''
Created on 2016年2月26日

@author: yupeng
'''
#python 表示符
#在python里，标识符有字母、数字、下划线组成。
#在python中，所有标识符可以包括英文、数字以及下划线（_），但不能以数字开头。
#python中的标识符是区分大小写的。
#以下划线开头的标识符是有特殊意义的。以单下划线开头（_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用"from xxx import *"而导入；
#以双下划线开头的（__foo）代表类的私有成员；以双下划线开头和结尾的（__foo__）代表python里特殊方法专用的标识，如__init__（）代表类的构造函数。

if True:
    print "True"
else:
    print "False"

counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

print counter
print miles
print name


# raw_input("Press the enter key to exit.")