# -*- coding: UTF-8 -*-
'''
Created on 2016年3月1日

@author: yupeng
'''

class Person:
    '''
    classdocs
    '''

    def sayHi(self):
        print 'hello world' + self.name

    def __init__(self, name=None):
        self.name = name
#     def __init__(self):
#         print 'hi 这是一个构造方法'

p = Person('12121');
print p
p.sayHi();


        
