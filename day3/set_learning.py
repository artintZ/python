# Author: zzk

# 集合set类似数学集合
list1 = set([1, 2, 3, 4, 5, 6, 7, 3, 5, 2, 1])
list2 = set([6, 7, 8, 9, 0, 2, 7, 3, 6, 4, 7])
list3 = list1.intersection(list2)

# 集合无重复元素
#list1 = set(list1)
# print(list1)

# 关系判断
# 交集
print(list1.intersection(list2, [2, 3, 4]))
print(list1 & list2 & {6})

# 并集
print(list1.union(list2))
print(list1 | list2)

# 差集 in list1 but not the others
print(list1.difference(list2, [1]))
print(list1 - list2 - {1})

# 对称差集 并集-交集
print(list1.symmetric_difference(list2))
print(list1 ^ list2)

# 子集、父集判断
print(list3.issubset(list1))
print(list3 <= list3)
print(list2.issuperset(list3))
# 不相交集判断
print(list1.isdisjoint([11]))

# 判断元素从属(同适用于字符串、列表、字典)
print('2' in '1121')
print(2 not in list1)

# 增
list1.add(9998)
#list1.update([2, 333])
list1.copy()  # 浅复制

# 删
list1.remove(9998)
list1.pop()
list1.discard(2)  # 如果元素是成员，则删除元素；否则不操作。
l = len(list1)  # 长度
print(list1, l)
