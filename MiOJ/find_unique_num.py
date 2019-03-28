# Author: zzk


import sys

for line in sys.stdin:
    l =line.strip().split()
    # for i in l:
    #     if l.count(i)==1:
    #         print(i)
    #         break
    single = 0
    for i in l:
        single = single^int(i)  # 异或
    print(single)
