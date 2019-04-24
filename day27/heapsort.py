# Author: zzk


def shift(data, low, high):
    i = low
    j = 2 * i + 1
    tmp = data[i]
    while j <= high:
        if j < high and data[j] < data[j + 1]:
            j += 1
        if tmp < data[j]:
            data[i] = data[j]
            i = j
            j = 2 * i + 1
        else:
            break
    data[i] = tmp


def heap_sort(data):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        shift(data, i, n - 1)
    for i in range(n-1, -1, -1):
        data[0], data[i]=data[i], data[0]
        shift(data, 0, i-1)
import random

l=list(range(10))
random.shuffle(l)
print(l)
heap_sort(l)
print(l)
