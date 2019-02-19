# Author: zzk


import random

print(random.random())  # [0, 1.0]随机浮点数
print(random.uniform(1, 5))  # [1, 5.0]随机浮点数
print(random.randint(10, 50))  # [10, 50]随机整数
print(random.randrange(5))  # 从range(5)中随机取出
# print(random.choice(sequence))  # 从字符串或列表、元组等有序类型中随机取出一个元素
# print(random.sample(sequence, k))  # 从有序类型中随机取出k个元素

# 洗牌
item = [1,2,3,4]
random.shuffle(item)
print(item)

# 生成验证码
checkcode = ''
for i in range(4):
    num = random.randrange(48, 58)
    char = random.randrange(65, 91)
    if random.randint(0, 1):
        checkcode+=chr(num)
    else:
        checkcode+=chr(char)
print(checkcode)