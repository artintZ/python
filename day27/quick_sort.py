# Author: zzk


import random

# 跟着我，右手左手一个慢动作，右手左手慢动作重播
def quick_sort(data, left, right):
    if left < right:
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data, mid + 1, right)


def partition(data, left, right):
    tmp = data[left]
    while left < right:
        while left < right and data[right] >= tmp:
            right -= 1
        data[left] = data[right]
        while left < right and data[left] <= tmp:
            left += 1
        data[right] = data[left]
    data[left] = tmp
    return left


l = list(range(100))
random.shuffle(l)
print(l)
quick_sort(l, 0, len(l) - 1)
print(l)
