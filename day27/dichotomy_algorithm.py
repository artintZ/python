# Author: zzk

import random


def bin_search(data_set, val):
    low = 0
    high = len(data_set)-1
    while low <= high:
        mid = (low + high)//2
        if data_set[mid] == val:
            return mid
        elif data_set[mid] < val:
            low = mid + 1
        else:
            high = mid-1
    return 0


l = list(range(10))
print(l)
# random.shuffle(l)
# print(l)
print(bin_search(l, 5))
