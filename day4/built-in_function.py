# Author: zzk

# python全部内置函数
print(abs(-1))  # 绝对值
print(all([-1, 0]), all([]))  # 可迭代对象元素都为真则返回True，空为True
print(any([-1, 0]), any([]))  # 可迭代对象元素有一个真则返回True，空为False
# print(type(ascii([1,2])))  # 转换成ASCII字符串
print(bin(255))  # 把整数转换成二进制
print(bool([1]), bool())  # 空的是False
# b = bytearray('abcd', encoding='utf-8')
# b[1] = 111
# print(b[0], b)  # 可修改的字节类型
# print(bytes('abcd', 'utf-8'))  # 字节类型
print(callable(abs))  # 函数等可加括号的可调用
print(chr(20320), ord('你'))  # Unicode中chr()返回对应字符，ord()返回对应码
# classmethod(abs)  # 把函数转换为类方法
# print(compile('a','','single'))  #
# print(complex(1,2))  # 复数
'''delattr() # 面向对象有用'''
# print(dict())  # 字典
print(dir([]))  # 返回数据类型可用方法
print(divmod(5, 2))  # 返回元组(商，余数)
# enumerate()  # 添加下标，返回可迭代
print(eval('1+2'))  # 可识别字符串内的数据格式
# print(exec(''))  # 类似eval()
'''
# res = filter(lambda n:n>4, range(8))  # 过滤
res = map(lambda n: n*2, range(8))  # 计算
for i in res:
    print(i)

import functools
res = functools.reduce(lambda x, y: y*x, range(1, 6))
print(res)  # 累加或累乘
'''
# print(float(2))  # 浮点数
# format()  # 格式化
# frozenset()  # 不可变的无序的可迭代
# print(globals())  # 返回当前文件全局变量名及其值
# print(locals())  # 返回局部变量名及其值
# getattr(),hasattr()  # 面向对象
print(hash('a'))  # 返回哈希值
# help()  #
print(hex(15))  # 十六进制
print(id('a'))  # 返回地址标识
# input()  # 默认字符串
# int()  # 整型
# print(isinstance('a', ()))  # 判断类型
# issubclass()  #
# iter()  # 迭代器
# len()  # 长度
# max(),min()  # 最大值
# memoryview()  #
# next()  # 作用于迭代器
# object()
# print(oct(8))  # 八进制
# open()  # 打开文件
print(pow(3, 2))  # 幂运算
# print()
# range()
# print(repr('a'))
# reversed()  # 反向
print(round(1.3456, 2))  # 四舍五入
# slice()  # 切片
# sorted()  # 排序
# staticmethod()  # 静态方法
# str()
print(sum([1,2]))  # 可迭代对象求和
# super()
# tuple()
# type()
# vars()
for i in zip([1,2,3],['a','b']):
    print(i)  # 合并
# __import__()
