# -*- coding: utf-8 -*-
#  class 派生类名（基类名）：//... 基类名写作括号里，基本类是在类定义的时候，在元组之中指明的。
'''在python中继承中的一些特点：
1：在继承中基类的构造（__init__()方法）不会被自动调用，它需要在其派生类的构造中亲自专门调用。
2：在调用基类的方法时，需要加上基类的类名前缀，且需要带上self参数变量。区别于在类中调用普通函数时并不需要带上self参数
3：Python总是首先查找对应类型的方法，如果它不能在派生类中找到对应的方法，它才开始到基类中逐个查找。（先在本类中查找调用的方法，找不到才去基类中找）。
如果在继承元组中列了一个以上的类，那么它就被称作"多重继承" 。'''

class Parent:   #定义父类
    parentAttr = 100
    def __init__(self):
        print '调用父类构造函数'
        
    def parentMethod(self):
        print '调用父类方法'
        
    def setAttr(self,attr):
        Parent.parentAttr = attr
        
    def getAttr(self):
        print '父类属性：',Parent.parentAttr
        
class Child(Parent):   #定义子类
    def __init__(self):
        print '调用子类构造方法'
        
    def childMethod(self):
        print '调用子类方法'
        
    def getAttr(self):   #方法重写
        print '调用子类方法'


    def __str__(self):   #用于将值转化为适于人阅读的形式
        return 'parentAttr %d' % (self.parentAttr)
        
        
c = Child()   #创建子类对象
c.childMethod()   #调用子类方法
c.parentMethod()   #调用父类方法
c.setAttr(200)   #调用父类方法修改parentAttr值
c.getAttr()   #调用父类方法
print c

#也可以继承多个类，如class C(A,B) 继承A和B

# issubclass() - 布尔函数判断一个类是另一个类的子类或者子孙类，语法：issubclass(sub,sup)
# isinstance(obj, Class) 布尔函数如果obj是Class类的实例对象或者是一个Class子类的实例对象则返回true。

'''方法重写'''
#如果你的父类方法的功能不能满足你的需求，你可以在子类重写你父类的方法
#如Child类里的getAttr()就是方法重写