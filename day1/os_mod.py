# Author: zzk

import os

os.system("dir")  # 打印当前文件夹下的目录，执行成功返回值0

cmd_res = os.popen("dir") # 返回值为地址
print(cmd_res)
print(cmd_res.read())  # read() 可读取地址指向的内容

#os.makedirs("new_dir")
os.mkdir("newdir")  # 在工作区新建文件夹