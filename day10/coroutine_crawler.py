# Author: zzk


import time
from urllib import request

import gevent
from gevent import monkey

monkey.patch_all()  # 给当前程序所有io操作做标记


def f(url):
    print('GET: %s' % url)
    resp = request.urlopen(url)
    data = resp.read()
    print('%d bytes received from %s.' % (len(data), url))


urls = ['https://www.python.org/',
        'https://www.yahoo.com/',
        'https://www.github.com/']

time_start = time.time()
for url in urls:
    f(url)

print('同步：', time.time()-time_start)
async_time_start = time.time()
gevent.joinall([
    gevent.spawn(f, urls[0]),
    gevent.spawn(f, urls[1]),
    gevent.spawn(f, urls[2])
])
print('异步：', time.time()-async_time_start)
