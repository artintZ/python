# Author: zzk

'''
import json

# json序列化，不同语言可以通用，只能处理简单数据类型
with open('dic', 'w', encoding='utf-8') as f:
    data = {
        'name': 'zzk',
        'age': '23'
    }
    f.write(json.dumps(data))

with open('dic', 'r', encoding='utf-8') as f:
    data = json.loads(f.read())
    print(data['name'])
'''

import pickle

# pickle序列化，只用于python
with open('dic', 'wb') as f:
    def foo():
        print('a')
    data = {
        'name': 'zzk',
        'age': '23',
        'func': foo
    }
    # f.write(pickle.dumps(data))
    pickle.dump(data,f)

with open('dic', 'rb') as f:
    # data = pickle.loads(f.read())
    data = pickle.load(f)
    data['func']()
