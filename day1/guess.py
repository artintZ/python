# Author: zzk

# while 循环语法示例，else 可选
import random

a = 400
b = 600
time = 15

age_of_zzk = random.randint(a, b)
cnt = 0
while cnt < time:
    guess_age = int(input("\n请输入400~600内的数字:"))
    if guess_age == age_of_zzk:
        print("你猜对了!\n")
        break
    elif guess_age < age_of_zzk:
        print("太小了!还剩{}次\n".format(time - cnt - 1))
    else:
        print("太大了!还剩{}次\n".format(time - cnt - 1))
    cnt = cnt + 1
else:  
    print("你的次数用完了!答案是{}".format(age_of_zzk))