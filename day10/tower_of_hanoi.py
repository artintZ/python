# Author: zzk

N = 4
l1 = []
l2 = []
l3 = []
for i in range(N, 0, -1):
    l1.append(i)

print(l1, l2, l3)


def move(sa, sc):
    global l1, l2, l3
    if sa == 'A' and sc == 'B':
        l2.append(l1.pop())
    elif sa == 'A' and sc == 'C':
        l3.append(l1.pop())
    elif sa == 'B' and sc == 'A':
        l1.append(l2.pop())
    elif sa == 'B' and sc == 'C':
        l3.append(l2.pop())
    elif sa == 'C' and sc == 'A':
        l1.append(l3.pop())
    else:
        l2.append(l3.pop())


def hanoi(n, a, b, c):
    if n == 1:
        print(a, '->', c)
        move(a, c)
    else:
        hanoi(n-1, a, c, b)
        print(a, '->', c)
        move(a, c)
        hanoi(n-1, b, a, c)


hanoi(N, 'A', 'B', 'C')
print(l1, l2, l3)
