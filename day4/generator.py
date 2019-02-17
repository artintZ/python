# Author: zzk

# generator生成器只有在调用的时候才会生成数据，\
# 且只记录当前数据，只有一个方法generator.__next__()
'''
a=(i**2 for i in range(10))
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())
for i in a:
    print(i*10)
'''

# 斐波那契数列
'''
def fib(max):
    n,a,b = 0,0,1
    while n<max:
        # print(b)
        yield b
        a,b = b,a+b
        n=n+1
    return 'done'

gen = fib(10)
while True:
    try:
        print(next(gen))
    except StopIteration as e:
        print(e)
        break
'''

# 协程

import time
def consumer():
    while True:
        n = yield
        if not n:
            print('ccccc')
            # return
        print('b',n)
        print('c', n)

def produce(c):
    c.__next__()
    for i in range(5):
        time.sleep(1)
        c.send(i)

c = consumer()
produce(c)