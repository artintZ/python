# Author: zzk


# 打印多行字符串,亦作多行注释
msg = '''
    name = "zzk"
    age = 22
    job = "student"
    '''
print(msg)

# 用户输入input()默认字符串类型
name = input("name =")
age = int(input("age ="))   # 函数int()转换为整型
print("name =", name, age)    # 逗号可以改成加号

# 多行字符串变量调用，方法一
info = '''
    ---info of %s---
    name = %s
    age = %d
    ''' %(name, name, age)
print(info)

# 多行字符串变量调用，方法二
info = '''
    ---info of {_name}---
    name = {_name}
    age = {_age}
    ''' .format(_name = name, _age = age)
print(info)

# 多行字符串变量调用，方法三
info = '''
    ---info of {0}---
    name = {0}
    age = {1}
    ''' .format(name, age)
print(info)