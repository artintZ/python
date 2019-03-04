# Author: zzk


# 封装
'''
class name(object):
    name = 'aaa'  # 类变量

    def __init__(self, name, *args, **kwargs):
        # 构造函数
        self.__name = name  # 实例变量  # 私有属性
        return super().__init__(*args, **kwargs)

    def print_name(self):
        print('My name is %s' % self.__name)


n1 = name('zzk')  # 实例化
# n1.name = 'zzk'
n1.print_name()
# name.name = 'ccc'
print(n1.name)
'''
'''
# 一切皆对象
def func(self):
    print('%s in the func'%self.name)


def __init__(self, name):
    self.name = name


Foo = type('Foo', (object,), {'func': func, '__init__': __init__})
f = Foo('zzk')
f.func()
'''


# 继承(广度优先)
'''
class People(object):
    def __init__(self, name, age, *args, **kwargs):
        # return super().__init__(*args, **kwargs)
        self.name = name
        self.age = age

    def eat(self):
        print('%s is eating...' % self.name)

    def sleep(self):
        print('%s is sleeping...' % self.name)

class Relation(object):
    def make_friends(self, obj):
        print('%s makes friends with %s'% (self.name, obj.name))

class Man(People):
    def working(self):
        print('%s is working...' % self.name)

    def sleep(self):
        People.sleep(self)
        print('man is sleeping')


class Woman(People, Relation):
    def __init__(self,name, age, money, *args, **kwargs):
        # People.__init__(self, name, age)
        super().__init__(name, age, *args, **kwargs)
        self.money = money

    def __del__(self):
        print('woman is done')

    def buy(self):
        print('%s is buying and takes %d 元...' % (self.name, self.money))


m1 = Man('zzk', 23)
w1 = Woman('ccc', 22, 10000)
# m1.sleep()
# w1.buy()
# m1.working()
w1.make_friends(m1)
'''

# 多态(一种接口，多重实现)


class Animal(object):
    def __init__(self, name, *args, **kwargs):
        self.name = name
        # super().__init__(*args, **kwargs)

    @staticmethod
    def animal_talk(obj):
        obj.talk()


class Dog(Animal):
    def talk(self):
        print('Woof!Woof!')


class Cat(Animal):
    def talk(self):
        print('Meow!')


d1 = Dog('ddd')
c1 = Cat('ccc')

Animal.animal_talk(d1)
Animal.animal_talk(c1)
# d1.talk()
# c1.talk()
