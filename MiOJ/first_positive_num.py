# Author: zzk


s = '3,4,-1,1'.split(',')
num='1'
while True:
    if num in s:
        num=str(int(num)+1)
    else:
        print(num)
        break