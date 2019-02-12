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
f = open('future', 'w')
f.write('hello world\n')
f.write('hello python')
f.close()
'''
# a可追加
'''
f = open('future', 'a')
f.write('\nhello dream')
f.close()
'''
