# Author: zzk

# 列表的增删改查基础操作
"""
# 列表list
names = ["a","b","c","d","e","f","g"]
# 增
names.append("e")  # 在列表末尾追加
names.insert(0,0)  # 在指定索引值位置插入
names2 = [1,2,3,4]
names.extend(names2)
# 改
names[3] = names[0] + 3  # 给列表指定位置重新赋值
# 删
del names[1]
names.remove(0)  # 删除第一个出现的元素
#names.pop()  # 丢掉（删除）默认最后一项
names.pop(1)  # 删除指定索引值的元素
#print(names.clear())  # 清空列表里的元素
# 查
print(names)
print(names[0],names[2])
print(names[1:3])  # 切片；顾头不顾尾
print(names[-1])  # -1表示最后一位
print(names[-3:])  # 切片；倒数前三位
print(names.index("e"))  # index()只返回从左到右搜索到的第一个索引值
print(names.count("e"))  # count()返回与括号内相同元素的个数
# 其他操作
names.reverse()  # 对列表里元素进行反转，无返回值
print(names[::-1])  # 对列表里元素进行反转
#names.sort()  # 对字符串按照ASCII码值排序：符号、数字、大写、小写；无返回值
print(names)
"""
# 复制列表
"""
import copy
names = ["a","b",[0,1,2],"c","d","e","f","g"]
#names2 = names.copy()  # copy()函数只复制列表第一层元素，第二层的元素被复制地址指针
#names2 = copy.copy(names)  # 浅copy，完全同上
names2 = names[:]  # 浅copy，完全同上
names2 = list(names)  # 浅copy，完全同上
names2 = copy.deepcopy(names)  # 深copy，把所有内存（包括指针指向的地址）都复制
names[1] = 'zzk'
names[2][1] = 'zzk'
print(names,names2)
"""
# 列表的循环操作
names = ["a","b",[0,1,2],"c","d","e","f","g"]
for i in names:
    print(i)
#for i in range(names.__len__()):
#    print(names[i])