# Author: zzk


class Cat(object):
    def __init__(self, name, *args, **kwargs):
        # return super().__init__(*args, **kwargs)
        self.name = name

    def sleep(self):
        print('%s is sleeping...' % self.name)


c = Cat('ccc')
# c.sleep()
l = []

try:
    # c.eat()
    # l[3]
    c.sleep()
except AttributeError as e:
    print(e)
except IndexError as e:
    print(e)
except Exception as e:  # 包含所有异常（除了缩进或语法错误）
    print(e)
else:
    print('Everything is OK.')
finally:
    print('错误与否都执行')