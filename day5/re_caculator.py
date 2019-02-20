# Author: zzk


import re

string_calc = '(a(b(c(d(e(f(g +g)))))))'
p1 = re.compile(r'[(]([a-z+\-*/ ]+)[)]')
a = p1.search(string_calc).group(0)
a=float('1')
print(a,type(a))

# 括号->除法->乘法->减法->加法 加号没了就打印退出