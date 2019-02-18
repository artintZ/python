# Author: zzk

import os
import sys

from day1 import guess_num

# import sys


# print(__file__)  # 当前文件的相对路径
# print(os.path.abspath(__file__))  # 当前文件的绝对路径
# print(os.path.dirname(os.path.abspath(__file__)))  # 当前文件的上一级目录

# # 当前文件的上上级目录
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)  # 添加环境变量


guess_num
