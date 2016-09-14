# -*- coding: utf-8 -*-
#coding utf-8

class Vector:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def __str__(self):   #用于将值转化为适于人阅读的形式
        return 'Vector (%d,%d)' % (self.a,self.b)
        
    def __add__(self,other):   #重新定义'+'号,运算符重载
        return Vector(self.a + other.a,self.b + other.b)
        
v1 = Vector(2,10)
v2 = Vector(5,-2)

print v1 + v2