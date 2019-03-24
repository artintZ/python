# Author: zzk


import threading
import time

event = threading.Event()


def light():
    cnt = 0
    event.set()  # green light
    while True:
        if cnt >= 5 and cnt < 10:
            event.clear()
            print('\033[41;1mred light\033[0m')
        elif cnt >= 10:
            cnt = 0
        else:
            event.set()
            print('\033[42;1mgreen light\033[0m')
        time.sleep(1)
        cnt += 1


def car(name):
    while True:
        if event.isSet():  # green light
            print('go go go')
            time.sleep(1)
        else:
            print('STOP!')
            event.wait()


light1 = threading.Thread(target=light,)
light1.start()

car1 = threading.Thread(target=car, args=('Tesla',))
car1.start()
