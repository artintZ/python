# Author: zzs2_index


# import sys

# q = "aabcc,dbbca,aadbbcbca"
q = 'aabcc,dbbca,aadbbcbcac'
[s1, s2, s3] = q.split(',')
if len(s1)+len(s2) != len(s3):
    print('false')
    exit(0)
for i in range(2):
    s1_index = s2_index = 0
    for num in s3:
        if s1_index < len(s1) and num == s1[s1_index]:
            s1_index += 1
        elif s2_index < len(s2) and num == s2[s2_index]:
            s2_index += 1
        else:
            if i == 1:
                print('false')
            break
    else:
        print('true')
        break
    s1, s2 = s2, s1

'''
import sys

for line in sys.stdin:
    [s1, s2, s3] = line.strip().split(',')
    if len(s1)+len(s2) != len(s3):
        print('false')
        exit(0)
    for i in range(2):
        s1_index = s2_index = 0
        for num in s3:
            if s1_index < len(s1) and num == s1[s1_index]:
                s1_index += 1
            elif s2_index < len(s2) and num == s2[s2_index]:
                s2_index += 1
            else:
                if i == 1:
                    print('false')
                break
        else:
            print('true')
            break
        s1, s2 = s2, s1
'''
