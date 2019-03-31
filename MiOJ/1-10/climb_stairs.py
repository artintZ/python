# Author: zzk


# 在你面前有一个n阶的楼梯，你一步只能上1阶或2阶。 
# 请问计算出你可以采用多少种不同的方式爬完这个楼梯

# n = '5'
n = '10'
def climb(n):
    if n<2:
        return 1
    else:
        return climb(n-1)+climb(n-2)
print(climb(int(n)))
