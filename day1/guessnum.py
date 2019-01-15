# Author: zzk

# while 循环语法示例，else 可选
age_of_zzk = 23
cnt = 0
while cnt < 3:
    guess_age = int(input("guess age of zzk:"))
    if guess_age == age_of_zzk:
        print("Bingo! You got it!")
        break
    elif guess_age < age_of_zzk:
        print("Too young!")
    else:
        print("Too old!")
    cnt = cnt + 1
else:
    print("What a pity!")

# for 循环语法示例，else 可选
age_of_zzk = 23
for cnt in range(3):
    guess_age = int(input("guess age of zzk:"))
    if guess_age == age_of_zzk:
        print("Bingo! You got it!")
        break
    elif guess_age < age_of_zzk:
        print("Too young!")
    else:
        print("Too old!")
else:
    print("What a pity!")