# Author: zzk


import hashlib

# md5加密
m = hashlib.md5()
m.update(b'hello world')
m.update(b'I am coming')
print(m.digest())
print(m.hexdigest())
m.update('世界那么大'.encode())
print(m.hexdigest())

# sha512加密
s512 = hashlib.sha512()
s512.update('我想去看看'.encode())
print(s512.hexdigest())