# Author: zzk

'''
执行方法：[python路径] file_modify.py 'find_str' 'replace_str'
'''

import sys

# 使用with语句可以自动关闭文件，注意冒号
with open('future', 'r', encoding='utf-8') as f,\
        open('future_new', 'w', encoding='utf-8') as f_new:
    find_str = sys.argv[1]
    replace_str = sys.argv[2]

    for line in f:
        if find_str in line:
            # line = 'hi'  # 整行赋值
            line = line.replace(find_str, replace_str)  # 指定内容赋值
        f_new.write(line)

# f.close()
# f_new.close()
