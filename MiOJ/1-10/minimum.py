# Author: zzk

'''
有一行由 N 个数字组成的数字字符串，字符串所表示的数是一正整数。
移除字符串中的 K 个数字，使剩下的数字是所有可能中最小的。
假设：
字符串的长度一定大于等于 K
字符串不会以 0 开头
'''
# [s, K] = '1432219 3'.split()
[s, K] = '10200 1'.split()
final_lenth = len(s)-int(K)
final_num=[]
start = 0
for n in range(final_lenth):
    final_num.append('9')
    for index in range(start, int(K)+n+1):
        if int(final_num[n]) > int(s[index]):
            final_num.pop()
            final_num.append(s[index])
            min_index = index
    start = index+1
minimum = ''
for i in final_num:
    minimum +=i
minimum = int(minimum)  # 去除高位的0
print(str(minimum))
