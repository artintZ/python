# Author: zzk


s = '2,3,1'.split(',')
cnt = 0
for i in range(len(s)-1):
    for j in range(len(s)-i-1):
        if int(s[j]) > int(s[j+1]):
            s[j], s[j+1] = s[j+1], s[j]
            cnt += 1
print(cnt)
