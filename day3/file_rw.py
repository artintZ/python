# Author: zzk

# data = open('future', 'r', encoding='utf-8').read()
# print(data)

# r只读
'''
# f为文件句柄
f = open('future', 'r', encoding='utf-8')
data = f.read(2)
print(data)
data2 = f.read(5)
print(data2)
f.close()
# read()读取是接着上次的开始
'''
# w覆盖原文件
'''
f = open('future', 'w', encoding='utf-8')
f.write('hello world\n')
f.write('hello python')
f.close()
'''
# a可追加
'''
f = open('future', 'a', encoding='utf-8')
f.write('\nhello dream')
f.close()
'''
# 按行读
'''
f = open('future', 'r', encoding='utf-8')
print(f.readline())
print(f.readline())
'''
# 循环行
'''
f = open('future', 'r', encoding='utf-8')
for line in f.readlines():  # readlines()每行作为一个元素组成列表
    print(line)
f.close()
'''

# 高效读取行循环打印
'''
f = open('future', 'r', encoding='utf-8')
cnt = 1
for line in f:
    if cnt >= 4:
        print('---分割线---')
    else:
        print(line)
    cnt = cnt + 1
'''
# 光标指定位置
'''
f = open('future','r', encoding='utf-8')
print(f.tell())  # 当前位置
print(f.readline())
print(f.tell())
print(f.seek(5))  # 指定光标位置
print(f.readline())
f.close()
'''
# 缓存写硬盘
'''
import sys
import time
f = open('future', 'w', encoding='utf-8')
# print(f.encoding)
for i in range(10):
    sys.stdout.write('#')
    sys.stdout.flush()  # 使缓存区内容写入硬盘
    time.sleep(0.5)
'''
# 截段
'''
f = open('future', 'a', encoding='utf-8')
# f.seek(2)  # 移动光标没用
f.truncate(10)
f.close()
'''
# r+读写，可控制光标读写
'''
f = open('future', 'r+', encoding='utf-8')
print(f.readline())
print(f.tell())
f.seek(0)
print(f.tell())
f.write('hello worldd')
print(f.tell())
print(f.readline())
#print(f.tell())
print(f.readline())
#print(f.tell())
f.close()
'''
# w+写读，tell和seek一起用可以控制写入位置（覆盖而不是插入）
'''
f = open('future', 'w+', encoding='utf-8')
#print(f.readline())
f.write('hello dream1\n')
#print(f.tell())
f.write('hello dream2\n')
#print(f.tell())
f.seek(0)
f.write('hello dream3\n')
#print(f.tell())
print(f.readline())
print(f.tell())
print(f.readline())
print(f.tell())
f.close()
'''
# # 二进制读写
# #'''
# f = open('future', 'rb')
# print(f.read())
# #f = open('future', 'wb')
# #f.write('hello \r\nbinary'.encode())

# 读取文件内容存入字典：读取部分必须是字典格式；列表同理
with open('future', 'r', encoding='utf-8') as f:
    string = f.read()
    string = eval(string)
    print(string)
    print(string[1])
