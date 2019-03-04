# Author: zzk


# 反射：把字符串映射到类的属性或方法 
class Dog(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print('%s is eating...' % self.name)


def bulk(self):
    print('%s is yelling...' % self.name)


d = Dog('ddd')
# d.eat()
method = input('>>')
if hasattr(d, method):  # 判断method是否为对象d的方法
    # func = getattr(d, method)  # 根据method调用d的方法
    # func()
    # attr = getattr(d, method)
    # delattr(d, method)  # 删除属性或方法
    setattr(d, method, 'ccc')
    print(d.name)
else:
    # setattr(d, method, bulk)  # 设置一个方法
    # bulk(d)
    # getattr(d, method)(d)
    pass
