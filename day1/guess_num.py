# Author: zzk

# while 循环语法示例，else 可选
import random

num_min = 400
num_max = 600
times = 10

num = random.randint(num_min, num_max)
cnt = 1
while cnt < times:
    guess_num = int(input("\n请输入{}~{}内的数字:".format(num_min, num_max)))
    if guess_num == num:
        print("你猜对了!\n")
        break
    elif guess_num < num:
        print("太小了!还剩{}次\n".format(times - cnt))
    else:
        print("太大了!还剩{}次\n".format(times - cnt))
    cnt = cnt + 1
else:  
    print("你的次数用完了!答案是{}".format(num))