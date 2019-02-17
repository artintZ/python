# Author: zzk

import time

'''高阶函数+嵌套函数->装饰器'''
# def timer(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         func()
#         stop_time = time.time()
#         print('the func runing time is %s' % (stop_time-start_time))
#     return wrapper

def decorator(type):
    def timer(func):
        def wrapper(*args, **kwargs):
            if type == 'a':
                start_time = time.time()
                func(*args, **kwargs)
                stop_time = time.time()
                print('the func runing time is %s' % (stop_time-start_time))
            else:
                func(*args,**kwargs)
                print('type is b')
        return wrapper
    return timer

@decorator('a')  # test1 = timer(test1)
def test1():
    time.sleep(1)
    print('in the test1')

@decorator('b')  # test2 = timer(test2)
def test2(s):
    time.sleep(1)
    print('in the %s'%(s))

test1()
test2('zzk')