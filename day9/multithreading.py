# Author: zzk


import threading
import time


def run(n):
    start_time = time.time()
    print('task', n)
    time.sleep(3)
    stop_time = time.time()
    print(stop_time-start_time)


t1 = threading.Thread(target=run, args=('1',))
t2 = threading.Thread(target=run, args=('2',))
t3 = threading.Thread(target=run, args=('3',))
t1.start()
t2.start()
t3.start()
# run('1')
# run('2')
# run('3')
class MyThread(threading.Thread):
    def __init__(self, n):
        self.n = n
        super().__init__()
    def run(self):
        print('running task', self.n)
        return super().run()

t1 = MyThread('1')
t2 = MyThread('2')
t1.start()
t2.start()