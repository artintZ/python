# Author: zzk


# 输入一个乱序的连续数列，输出其中最长连续数列长度，要求算法复杂度为 O(n) 。
s = '5,4,3,2,1'

s = s.split(',')
s.sort(key=int)
print(s)
temp=max = 1
for i in range(len(s)-1):
    if int(s[i+1])-int(s[i])==1:
        temp +=1
    elif max<temp:
        max=temp
    else:
        pass
if max<temp:
    print(temp)
else:
    print(max)
