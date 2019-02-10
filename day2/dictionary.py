# Author: zzk

# key-value
info = {
    1: 'a',
    2: 'b',
    'stu1': 'c',
    'stu2': 'd'
}

# 增
info[3] = 'c'
info['stu3'] = 'ggg'
# 删
#del info['stu1']
#print(info.pop(1))  # 删除指定键及值，并返回值
#print(info.popitem())  # 删除随机键值并返回其组成的元组
# 改
info['stu2'] = 'ddd'
# 查
print(info)
print(info[2])
print(info.get('stu3'))  # 返回键的值，没有返回None
print(2 in info)  # 判断键是否在info
print(info.keys())
print(info.values())
# 字典的嵌套
info['china'] = {'shandong': 'jining'}
print(info.get('china'))
print(info)
print(info['china']['shandong'])
print(info.setdefault('jining','jiaxiang'))  # 键值存在则不改，否则添加
info.update({1:"a", 'jining':'jining'})  # 更新字典info，键存在则覆盖，否则添加
print(info.items())  # dictionary -> list [(key, value)]

test = dict.fromkeys([1,2,3,4], [1,2])  # 新建列表值是一样的，浅复制
test[1][0] = 2
test[1] = 11
print(test)

# for循环打印
for i in info:  # i只取key
    print(i, info[i])
#for k,v in info.items():  # 需要先把字典转换为列表，低效
#    print(k, v)