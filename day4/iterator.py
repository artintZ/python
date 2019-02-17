# Author: zzk

# 可以直接作用于for循环的对象为可迭代对象iterable
'''
from collections import Iterable

print(isinstance({}, Iterable))
print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance('a', Iterable))
print(isinstance((x for x in range(5)), Iterable))
# print(isinstance(100, Iterable))
'''
 
# 可以用next()函数调用并且不断返回下一个值的对象为迭代器iterator

from collections import Iterator

print(isinstance(iter({}), Iterator))
print(isinstance(iter([]), Iterator))
print(isinstance(iter(()), Iterator))
print(isinstance(iter('a'), Iterator))
print(isinstance((x for x in range(5)), Iterator))
# print(isinstance(100, Iterable))
