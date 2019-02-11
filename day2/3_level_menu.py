# Author: zzk

# 最后一级菜单用列表而不是单纯的字符串，便于统一打印
data = {
    'China': {
        'shandong': {'jining':['606'], 'jinan':['friends']},
        'shanghai': {'yangpu':['USST'], 'pudong':['mingzhu']}
    },
    'America': {
        'Alaska': ['阿拉斯加'],
        'California': ['加利福尼亚']
    }
}

while True:
    for i in data:
        print(i)
    choice1 = input('（b返回,q退出）请选择菜单：')
    if choice1 in data:
        
        while True:
            for i in data[choice1]:
                print(i)
            choice2 = input('（b返回,q退出）请选择菜单：')
            if choice2 in data[choice1]:
                
                while True:
                    for i in data[choice1][choice2]:
                        print(i)
                    choice3 = input('（b返回,q退出）请选择菜单：')
                    if choice3 in data[choice1][choice2]:
                        
                        while True:
                            for i in data[choice1][choice2][choice3]:
                                print(i)
                            
                            choice4 = input('按b返回,按q退出：')
                            if choice4 == 'b':
                                break
                            elif choice4 == 'q':
                                exit('退出')
                    elif choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit('退出')
                    else:
                        print('错误！找不到选项\n')
                        continue
            elif choice2 == 'b':
                break
            elif choice2 == 'q':
                exit('退出')
            else:
                print('错误！找不到选项\n')
                continue
    elif choice1 == 'b':
        break
    elif choice1 == 'q':
        exit('退出')
    else:
        print('错误！找不到选项\n')
        continue
