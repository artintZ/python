# Author: zzk


import queue


q = queue.Queue()  # first in first out

q.put(1)
q.put(2)
q.put(3)

print(q.get())
print(q.get())
print(q.get())

q = queue.LifoQueue()  # last in first out

q.put(1)
q.put(2)
q.put(3)

print(q.get())
print(q.get())
print(q.get())

q = queue.PriorityQueue()  # 元组排序

q.put(('d', 2))
q.put(('c', 5))
q.put(('a', 7))
q.put(('b', 9))

print(q.get())
print(q.get())
print(q.get())
print(q.get())
