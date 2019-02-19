# Author: zzk


import configparser

# 写入配置文件
config = configparser.ConfigParser()
# config['DEFAULT'] = {'a': 1, 'b': 2, 'c': 3}
# config['bitbucket.org'] = {}
# config['bitbucket.org']['User'] = 'hg'
# config['topsecret.server.com'] = {}
# secret = config['topsecret.server.com']
# secret['ddd'] = '444'

# with open('example.ini', 'w') as configfile:
#     config.write(configfile)

# 解析配置文件
config.read('example.ini')
print(config.defaults())
print(config.sections())
print(config['bitbucket.org']['User'])
