# Author: zzk


class Person(object):
    '''描述人的，包括姓名、年龄等'''
    def __init__(self, name, age, *args, **kwargs):
        self.name = name
        self.age = age
        # return super().__init__(*args, **kwargs)
    def print_info(self):
        print(self.name, self.age)

    def __call__(self):
        print('in the call')

p = Person('zzk', 23)
p.print_info()

print(p.__doc__)  # 类的描述信息
print(p.__module__)  # 当前对象在哪个模块
print(p.__class__)  # 当前对象在哪个类
p()  # __call__方法
print(p.__dict__)  # 对象的实例属性
# __setitem__  # 把实例变成字典

