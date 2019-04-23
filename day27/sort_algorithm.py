# Author: zzk

import random


def bubble_sort(l):
    for i in range(len(l)-1):
        exchange = False
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                exchange = True
        if not exchange:
            break


def select_sort(l):
    for i in range(len(l)-1):
        min_loc = i
        for j in range(i+1, len(l)):
            if l[min_loc] > l[j]:
                min_loc = j
        l[i], l[min_loc] = l[min_loc], l[i]


def insert_sort(l):
    for i in range(1, len(l)):
        tmp = l[i]
        j = i
        while j > 0 and l[j-1] > tmp:
            l[j] = l[j-1]
            j = j-1
        l[j] = tmp


l = list(range(10))
random.shuffle(l)
print(l)
# bubble_sort(l)
# select_sort(l)
insert_sort(l)
print(l)
