# Author: zzk


def merge(data, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if data[i] < data[j]:
            ltmp.append(data[i])
            i += 1
        else:
            ltmp.append(data[j])
            j += 1
    while i <= mid:
        ltmp.append(data[i])
        i += 1
    while j <= mid:
        ltmp.append(data[j])
        j += 1
    data[low:high] = ltmp


def merge_sort(data, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(data, low, mid)
        merge_sort(data, mid + 1, high)
        merge(data, low, mid, high)


import random

l = list(range(10))
random.shuffle(l)
print(l)
merge_sort(l, 0, len(l) - 1)
print(l)
