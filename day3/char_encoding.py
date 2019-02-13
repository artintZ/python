# Author: zzk

s = '你好梦想'  # unicode
s_utf8 = s.encode()
s_gbk = s.encode('gbk')
print(s_utf8, s_utf8.decode())
print(s_gbk, s_gbk.decode('gbk'))
