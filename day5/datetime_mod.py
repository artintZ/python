# Author: zzk

import datetime
import time

# 时间加减
print(datetime.datetime.now())  # 返回 2019-02-19 13:12:26.941925
print(datetime.date.fromtimestamp(time.time()))  # 时间戳转日期格式 2019-02-19
print(datetime.datetime.now() + datetime.timedelta(3))  # 当前时间+3天
print(datetime.datetime.now() + datetime.timedelta(-3))  # 当前时间-3天
print(datetime.datetime.now() + datetime.timedelta(hours=3))  # 当前时间+3小时
print(datetime.datetime.now() + datetime.timedelta(minutes=30))  # 当前时间+30分钟
print(datetime.datetime.now().replace(minute=30, hour=5))  # 时间替换
