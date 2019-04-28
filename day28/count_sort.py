# Author: zzk


def count_sort(data, max_num):
    # count = [0] * (max_num + 1)
    count = [0 for i in range(0, max_num + 1)]
    for num in data:
        count[num] += 1
    index = 0
    for num, m in enumerate(count):
        for i in range(m):
            data[index] = num
            index += 1


import random

result = []
for i in range(100):
    l = random.randrange(10)
    result.append(l)
print(result)
count_sort(result, 9)
print(result)
