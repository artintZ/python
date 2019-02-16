# Author: zzk

# *args接收不确定的多个位置参数，到元组

'''
def test(*args):
    print(args)


test([1, 2], 3, *[4, 5], 6)
'''

# **kwargs接收关键字参数，到字典
'''
def test(**kwargs):
    print(kwargs['a'])


test(a=1, b=2, c=3, **{'aab':5})
'''

# 递归函数

'''
def factorial(n):
    if n<= 1:
        return 1
    else:
        return n*factorial(n-1)


print(factorial(-3))
'''
'''
def calc(n):
    if n<=0:
        return 0
    else:
        print(n)
        return calc(int(n/2))
    
# calc(10)

# 匿名函数
res = map(lambda n:n**2,[2,5,10,16])
for i in res:
    print(i)
'''

# 高阶函数


def add(a, b):
    return a+b


def abstract(a, b):
    return a-b


def print_num(a, b, f):
    print(f(a, b))


print_num(6, 3, add)
print_num(6, 3, abstract)
