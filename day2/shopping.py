# Author: zzk

goods = (('手机', 3000), ('电脑', 8000), ('汽车', 150000),
         ('餐具', 300), ('家具', 20000), ('家电', 30000))
goods_sold = []
SALARY = int(input('请输入你的工资:'))
BALANCE = SALARY

def menu():
    print('\n编号','商品',' 价格')
    for i in range(goods.__len__()):
        print('\n', i + 1,'、', end = '')
        for j in range(2):
            print(goods[i][j],' ', end = '')
    print('\n 0 、退出')
    n = int(input('请输入想要购买的商品的编号:'))
    return n

def buy(n):
    global BALANCE
    if goods[n - 1][1] <= BALANCE:
        BALANCE = BALANCE - goods[n - 1][1]
        goods_sold.append(goods[n - 1])
        print('购买成功！花了{}元，余额为{}元'.format(goods[n-1][1], BALANCE))
    else:
        print('余额不足！价格为{}元，余额为{}元'.format(goods[n-1][1], BALANCE))
    input()

def balance():
    print('\n购物清单：')
    for i,(j,k) in enumerate(goods_sold):
        print(i, j, k)
    print('您一共消费{}元，您的余额{}元'.format(SALARY - BALANCE, BALANCE))
    input('按任意键退出')

while 1:
    n = menu()
    if n:
        buy(n)
    else:
        break
balance()
    



