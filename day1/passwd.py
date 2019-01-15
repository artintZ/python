# Author: zzk

"""
# 密码为密文（在 python 解释器中可行）

import getpass

usrname = input("usrname:")
passwd = getpass.getpass("passwd:")
print(usrname, passwd)
"""

# if-else 的基础示例及简单嵌套

_usrname = "zzk"
_passwd = "zzk"

usrname = input("usrname:")
passwd = input("passwd:")

if _usrname == usrname and _passwd == passwd:
    print("Welcome user {} to login...".format(usrname))
elif _usrname == usrname:
    print("Wrong password!")
else:
    print("Wrong username!")