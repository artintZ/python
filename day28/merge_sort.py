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
    while j <= high:
        ltmp.append(data[j])
        j += 1
    data[low : high + 1] = ltmp


def merge_sort(data, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(data, low, mid)
        merge_sort(data, mid + 1, high)
        merge(data, low, mid, high)


def MergeSort(lists):
    if len(lists) <= 1:
        return lists
    num = len(lists) // 2
    left = MergeSort(lists[:num])
    right = MergeSort(lists[num:])
    return Merge(left, right)


def Merge(left, right):
    r, l = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += list(left[l:])
    result += list(right[r:])
    return result


import random

l = list(range(10))
random.shuffle(l)
print(l)
# l = MergeSort(l)
merge_sort(l, 0, len(l) - 1)
print(l)
