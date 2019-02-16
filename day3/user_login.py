# Author: zzk

import os


def lock(usrname, tag_old='#', tag_new='$'):
    '''锁定用户，即把标识#换成$'''
    id_normal = tag_old.join(['', usrname, ''])
    id_locked = tag_new.join(['', usrname, ''])
    with open('id_data', 'r', encoding='utf-8') as f,\
            open('id_data.bak', 'w', encoding='utf-8') as f_new:
        for line in f:
            if id_normal in line:
                line = line.replace(id_normal, id_locked)
            f_new.write(line)
    os.remove('id_data')
    os.rename('id_data.bak', 'id_data')
    if tag_old == '#':
        print('用户已被锁定，请联系管理员解锁！\n')
    else:
        print('用户已解锁，可以正常登录！\n')


def unlock(usrname):
    '''解锁用户'''
    lock(usrname, tag_old='$', tag_new='#')


def isstatus(usrname):
    '''判断用户状态，若已注册且状态正常则返回1，\
        已注册并且被锁定返回2，未被注册返回0'''
    with open('id_data', 'r', encoding='utf-8') as f:
        for line in f:
            if usrname.join(['#', '#']) in line:
                return 1
            elif usrname.join(['$', '$']) in line:
                return 2
        else:
            return 0


def iscorrect(usrname, passwd):
    '''判断用户名和密码是否正确，正确就返回1，否则返回0'''
    id_normal = '#'.join(['', usrname, passwd, ''])
    with open('id_data', 'r', encoding='utf-8') as f:
        for line in f:
            if id_normal in line:
                return 1
        else:
            return 0


def register():
    '''注册，在文件中添加用户名和密码'''
    while True:
        print('\n\n', '注册/按b返回'.center(20, '-'))
        usrname = input('请设置用户名：')
        if usrname == 'b':
            break
        elif len(usrname) < 3:
            print('用户名至少三个字符,请重新输入！\n')
        elif isstatus(usrname):
            print('用户名已被注册，请重新输入！\n')
        else:
            passwd = input('请设置密码/按b返回：')
            if passwd == 'b':
                break
            with open('id_data', 'a', encoding='utf-8') as f:
                id_normal = '#'.join(['', usrname, passwd, '\n'])
                f.write(id_normal)
            print('\n注册成功！返回主菜单……\n\n')
            break


def delete():
    '''删除文件中的用户名和密码：新建文件修改，再删除原文件并重命名新文件'''
    while True:
        print('\n\n', '删除/按b返回'.center(20, '-'))
        usrname = input('请输入用户名：')
        if usrname == 'b':
            break
        elif not isstatus(usrname):
            print('用户名不存在，请重新输入！\n')
        else:
            with open('id_data', 'r', encoding='utf-8') as f,\
                    open('id_data.bak', 'w', encoding='utf-8') as f_new:
                for line in f:
                    if usrname.join(['#', '#']) in line\
                            or usrname.join(['$', '$']) in line:
                        continue
                    f_new.write(line)
            os.remove('id_data')
            os.rename('id_data.bak', 'id_data')
            print('删除成功\n')


def admin_menu():
    """管理员菜单，返回值'1. 添加', '2. 删除',\
        '3. 解锁', '4. 锁定', '5. 查询', '0. 退出'"""
    menu = ('1. 添加', '2. 删除', '3. 解锁',
            '4. 锁定', '5. 查询', '0. 退出')
    print('\n\n', '管理界面'.center(20, '-'))
    for i in menu:
        print(i)
    while True:
        choice = input('\n请输入你的选择：')
        if choice.isdigit() and int(choice) in range(6):
            return int(choice)
        else:
            print('输入不正确，请重新输入！\n')


def administrator():
    '''管理员操作过程，包括添加，删除，解锁，上锁，查询，退出'''
    while True:
        choice = admin_menu()
        if choice == 1:
            register()
        elif choice == 2:
            delete()
        elif choice == 3:
            while True:
                print('\n\n', '解锁/按b返回'.center(20, '-'))
                usrname = input('请输入用户名')
                if usrname == 'b':
                    break
                elif isstatus(usrname) == 2:
                    unlock(usrname)
                else:
                    print('该用户无需解锁！\n')
                    break
        elif choice == 4:
            while True:
                print('\n\n', '上锁/按b返回'.center(20, '-'))
                usrname = input('请输入用户名')
                if usrname == 'b':
                    break
                elif isstatus(usrname) == 1:
                    lock(usrname)
                else:
                    print('该用户无需上锁！\n')
                    break
        elif choice == 5:
            while True:
                print('\n\n', '查询/按b返回'.center(20, '-'))
                usrname = input('请输入用户名：')
                if usrname == 'b':
                    break
                elif isstatus(usrname) == 1:
                    print('该用户状态正常。\n')
                elif isstatus(usrname) == 2:
                    print('该用户已被锁定。\n')
                else:
                    print('没有找到该用户！\n')
        else:
            exit()


def login():
    '''登录过程，用户和管理员登录'''
    while True:
        print('\n\n', '登录界面/按b返回'.center(20, '-'))
        usrname = input('请输入用户名：')
        if usrname == 'b':
            break
        elif usrname == 'admin':
            for cnt in range(3):
                passwd = input('请输入管理员密码：')
                if passwd == 'admin':
                    administrator()
                else:
                    print('密码错误 %d 次，错误三次返回主菜单！\n' % (cnt+1))
            else:
                break
        elif isstatus(usrname) == 1:
            for cnt in range(3):
                passwd = input('请输入密码/按b返回：')
                if passwd == 'b':
                    break
                elif iscorrect(usrname, passwd):
                    exit('登录成功！正在退出……')
                else:
                    print('密码错误 %d 次，错误三次锁定用户！\n' % (cnt+1))
            else:
                lock(usrname)
        elif isstatus(usrname) == 2:
            print('用户已被锁定，请联系管理员解锁！\n')
        else:
            print('用户名不存在，请先注册！\n')


def main_menu():
    """主菜单，返回值'1. 登录', '2. 注册', '0. 退出'"""
    menu = ('1. 登录', '2. 注册', '0. 退出')
    print('\n\n', '主界面'.center(20, '-'))
    for i in menu:
        print(i)
    while True:
        choice = input('\n请输入你的选择：')
        if choice.isdigit() and int(choice) in range(3):
            return int(choice)
        else:
            print('输入不正确，请重新输入！\n')


# 主函数
while True:
    choice = main_menu()
    if choice == 1:
        login()
    elif choice == 2:
        register()
    else:
        exit()
