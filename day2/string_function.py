# Author: zzk

msg = 'i like zzk'

print(msg.capitalize())  # 首字母大写
print(msg.count('k'))  # 返回字符串中‘k’的个数
print(msg.center(20, '*'))  # 把msg放中间，填充‘*’总宽度为20
print(msg.endswith('zk'))  # 判断是否以zk结尾，返回True或False
print(msg.startswith('i'))  # 判断是否以i开头，返回True或False
print(msg.find('zz'))  # 从左开始找到zz返回起始索引值
print(msg.rfind('zz'))  # 从右开始找zz返回正序索引值
print(msg[7:-1])  # 切片，类似列表
for i in msg:
    print(i)

print('aB24'.isalnum())  # 判断是否为字母或数字
print('aB'.isalpha())  # 判断是否为字母
print(msg.islower())  # 判断是否小写字母
print('ABCD'.isupper())  # 判断是否大写字母
print('24'.isdigit())  # 判断是否为数字
print('12ab'.isidentifier())  # 判断是否合法字符
print(msg.istitle())  # 判断是否每个单词首字母大写
print('    '.isspace())  # 判断是否空格
print(' + '.join(['I', 'you', 'it']))  # 把字符串合并到列表
print(msg.ljust(20, '*'))  # 从左边开始msg，宽带20，填充*
print(msg.rjust(20, '*'))  # 从右边开始msg，宽带20，填充*
print(msg.upper())  # 把小写字母改成大写
print('ABDHJ'.lower())  # 把大写字母改成小写
print(msg.swapcase())  # 大小写字母反转
print(msg.title())  # 把msg改成标题形式
print('\n  \nfff\n  \n'.lstrip())  # 去掉左侧换行和空格
print('\n\nfff\n\n  '.rstrip())  # 去掉右侧换行和空格
print('\n\nf\nf  f\n     \n'.strip())  # 去掉两端的换行和空格

# 一个参数必须是字典；两个参数必须是字数相同的字符串；最后一个参数映射到空。
# 若有重复(非函数映射)以后面的映射为准
# maketrans()返回用于translate()的翻译表
p = str.maketrans('abckefghijklmn','111116789A1CDE','z')
print(msg.translate(p))

print(msg.replace('k', '1', 1))  # 从左往右替换1个

print('1+2+3+4'.split('+'))  # 把字符串拆成列表，以+为分界线（删掉+）

