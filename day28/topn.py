# Author: zzk


def shift(data, start, end):  # 小根堆
    root = start
    child = root * 2 + 1
    tmp = data[root]
    while child <= end:
        if child < end and data[child] > data[child + 1]:
            child += 1
        if tmp > data[child]:
            data[root] = data[child]
            root = child
            child = root * 2 + 1
        else:
            break
    data[root] = tmp


def topn(data, n):
    heap = data[0:n]
    # 建堆
    for i in range(n // 2 - 1, -1, -1):
        shift(heap, i, n - 1)
    # 遍历
    for i in range(n, len(data)):
        if data[i] > heap[0]:
            heap[0] = data[i]
            shift(heap, 0, n - 1)
    # 出数
    for i in range(n - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        shift(heap, 0, i - 1)
    return heap


import random

l = list(range(1000))
random.shuffle(l)
# print(l)
l = topn(l, 10)
print(l)

