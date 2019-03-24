# Author: zzk


import queue
import threading
import time
q = queue.Queue(maxsize=10)


def Producer(name):
    cnt =0
    while True:
        cnt+=1
        q.put('骨头%s'%cnt)
        print('[%s] 生产了骨头 %s'% (name, cnt))
        time.sleep(1)


def Consumer(name):
    while True:
        print('[%s] 吃了 [%s]' % (name, q.get()))
        time.sleep(1.5)

p = threading.Thread(target=Producer, args=('zzk',))
c = threading.Thread(target=Consumer, args=('ccc',))
c1 = threading.Thread(target=Consumer, args=('ddd',))

p.start()
c.start()
c1.start()