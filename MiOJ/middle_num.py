# Author: zzk


# 找出旋转有序数列的中间值
import sys

s='4,5,6,7,0,1,2'
# for line in sys.stdin:
s = s.strip().split(',')
s.sort(key=int)
print(s[int((len(s)-1)/2)])