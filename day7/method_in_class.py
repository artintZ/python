# Author: zzk


class Person(object):
    name = 'ccc'

    def __init__(self, name, *args, **kwargs):
        self.name = name
        # return super().__init__(*args, **kwargs)

    # @staticmethod  # 在类中但与类没有关系，不能访问类变量和实例变量
    # @classmethod  # 只能访问类变量

    @property  # 使方法变成一个属性
    def eat(self):
        print('%s is eating...' % self.name)

    @eat.setter
    def eat(self, name):
        print('set name:', name)
        self.name = name

    @eat.deleter
    def eat(self):
        del self.name

p = Person('zzk')
p.eat
p.eat = 'a'
p.eat
del p.eat
p.eat
