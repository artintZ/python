# Author: zzk


def shell_sort(data):
    gap = len(data) // 2
    while gap > 0:
        for i in range(gap, len(data)):
            tmp = data[i]
            j = i - gap
            while j >= 0 and tmp < data[j]:
                data[j + gap] = data[j]
                j -= gap
            data[j + gap] = tmp
        gap //= 2


# 时间复杂度O(1.3n)
import random

l = list(range(11))
random.shuffle(l)
print(l)
shell_sort(l)
print(l)
