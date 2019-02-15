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
# lock('zzk','zzk')


def unlock(usrname):
    '''解锁用户'''
    lock(usrname, tag_old='$', tag_new='#')


# unlock('zzk', 'zzk')

def islocked(usrname):
    '''判断用户是否锁定，若锁定则返回1，否则返回0'''
    with open('id_data', 'r', encoding='utf-8') as f:
        for line in f:
            if usrname.join(['$', '$']) in line:
                return 1
        else:
            return 0
# unlock('zzk')
# print(islocked('zzk'))


def username():
    '''返回未被注册的用户名'''
    with open('id_data', 'r', encoding='utf-8') as f:
        while True:
            usrname = input('请输入用户名：')
            if usrname == 'b':
                break
            else:
                for line in f:
                    if usrname.join(['#', '#']) in line\
                        or usrname.join(['$', '$']) in line:
                        print('用户名已被注册，请重新输入！\n')
                        break
                else:
                    return usrname
    


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
        usrname = input('请设置用户名：')
        if usrname == 'b':
            break
        elif username(usrname):
            print('用户名已被注册，请重新输入！')
        else:
            passwd = input('请设置密码：')
            with open('id_data', 'a', encoding='utf-8') as f:
                id_normal = '#'.join(['', usrname, passwd, '\n'])
                f.write(id_normal)
            print('\n注册成功！返回主菜单……\n\n')
            break

# register('a', 'b')


def delete(usrname):
    '''删除文件中的用户名和密码'''
    with open('id_data', 'r', encoding='utf-8') as f,\
            open('id_data.bak', 'w', encoding='utf-8') as f_new:
        for line in f:
            if usrname.join(['#', '#']) in line\
                    or usrname.join(['$', '$']) in line:
                continue
            f_new.write(line)
    os.remove('id_data')
    os.rename('id_data.bak', 'id_data')

# delete('hello')


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
            print('\n\n', '管理员添加/按b返回'.center(20, '-'))
            register()
        elif choice == 2:
            print('\n\n', '管理员删除/按b返回'.center(20, '-'))
            delete()


def main_menu():
    """主菜单，返回值'1. 登录', '2. 注册', '0. 退出'"""
    menu = ('1. 登录', '2. 注册', '0. 退出')
    print('主界面'.center(20, '-'))
    for i in menu:
        print(i)
    while True:
        choice = input('\n请输入你的选择：')
        if choice.isdigit() and int(choice) in range(3):
            return int(choice)
        else:
            print('输入不正确，请重新输入！\n')

# print('0' in ['2'] or '2' in ['0'])


# 主函数
while True:
    choice = main_menu()
    if choice == 1:
        print('\n\n', '登录界面'.center(20, '-'))
        usrname = input('请输入用户名：')
        if usrname == 'admin':
            for cnt in range(3):
                passwd = input('请输入管理员密码：')
                if passwd == 'admin':
                    while True:
                        choice = admin_menu()
                        '''if choice == 1:
                            print('\n\n', '管理员添加界面/按b返回'.center(20, '-'))
                            register()'''

                else:
                    print('密码错误 %d 次，错误三次返回主菜单！\n' % (cnt+1))
        elif not username(usrname):
            print('用户名不存在，请先注册！\n')
        elif islocked(usrname):
            print('用户已被锁定，请联系管理员解锁！\n')
        else:
            for cnt in range(3):
                passwd = input('请输入密码：')
                if iscorrect(usrname, passwd):
                    print('登录成功！正在退出……')
                    exit()
                else:
                    print('密码错误 %d 次，错误三次锁定用户！' % (cnt+1))
            else:
                lock(usrname)
                print('用户已被锁定，请联系管理员解锁！\n')
    elif choice == 2:
        print('\n\n', '注册界面/按b返回'.center(20, '-'))
        register()
    else:
        exit()

# 优化判断用户名是否存在和锁定！！！！！！！！！！！！！