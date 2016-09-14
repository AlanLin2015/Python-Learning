# coding:utf-8

class JustCounter:
    __secretCount = 0   #私有变量
    publicCount = 0   #公开变量
    
    def count(self):
        self.__secretCount += 1 
        self.publicCount += 1
        print self.__secretCount
        
counter = JustCounter()
counter.count()
counter.count()
print counter.publicCount
#print counter.__secretCount   #此处报错，不能在类外部调用私有属性
print counter._JustCounter__secretCount   #可以用object._className__attrName来访问属性

