# Author: zzk

#import os


def login():
    for i in range(3):
        usrname = input('请输入用户名：')
        passwd = input('请输入密码：')
        id_string = '#'.join(['', usrname, passwd, ''])
        if id_string == '#admin#admin#':
            return 1
        with open('future', 'r') as f:
            for line in f:
                if id_string in line:
                    print('welcome %s', usrname)

# 判断嵌套，依次判断用户名、密码
login()
