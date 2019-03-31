# Author: zzk


# import sys

q = "aabcc,dbbca,aadbbcbca"
q = q.split(',')
if len(q[0])+len(q[1])!=len(q[2]):
    print('false')
    exit(0)
j = k = 0
for i in q[2]:
    if j < len(q[0]) and i == q[0][j]:
        j += 1
    elif k < len(q[1]) and i == q[1][k]:
        k += 1
    else:
        # print('false')
        break
else:
    print('true')
    exit(0)

j = k = 0
for i in q[2]:
    if k < len(q[1]) and i == q[1][k]:
        k += 1
    elif j < len(q[0]) and i == q[0][j]:
        j += 1
    else:
        print('false')
        break
else:
    print('true')

'''
import sys

for line in sys.stdin:
    q = line.strip().split(',')
    j = k = 0
    for i in q[2]:
        if j < len(q[0]) and i == q[0][j]:
            j += 1
        elif k < len(q[1]) and i == q[1][k]:
            k += 1
        else:
            # print('false')
            break
    else:
        print('true')
        continue

    j = k = 0
    for i in q[2]:
        if k < len(q[1]) and i == q[1][k]:
            k += 1
        elif j < len(q[0]) and i == q[0][j]:
            j += 1
        else:
            print('false')
            break
    else:
        print('true')
'''

