# Author: zzk

import sys

# 打印环境变量path（把模块放入这些path中，通过import就可以导入）
print(sys.path)

"""
# sys.argv 可在外部向程序内部传递参数
print(sys.argv[0])
print(sys.argv[1])
# 在终端运行 python sys_mod.py hello
# 结果为
sys_mod.py  #相对路径
hello
"""