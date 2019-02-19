# Author: zzk


import shelve

d = shelve.open('file_name')  # 打开一个文件

# info_dict = {'age': 23,'job': 'IT'}
# name_list = ['a', 'b', 'c']
# def foo_func():
#     return 'in the foo'

# d['name'] = name_list  # 持久化列表
# d['info'] = info_dict  # 持久化字典
# d['foo'] = foo_func()  # 持久化函数
# d.close()

print(d.get('name'))
print(d.get('info'))
print(d.get('foo'))
d.close()