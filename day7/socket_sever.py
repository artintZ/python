# Author: zzk


import socket

sever = socket.socket()
sever.bind(('localhost', 6969))  # 绑定要监听端口
sever.listen()  # 监听

conn, addr = sever.accept()

data = conn.recv(1024)

print(data)
conn.send(data.upper())

sever.close()

