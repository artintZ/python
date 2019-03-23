# Author: zzk


import socket

client = socket.socket()  # 声明socket类型，同时生成socket连接对象
client.connect(('localhost', 9999))
while True:
    msg = input().strip()
    if len(msg) == 0:
        continue
    client.send(b'client:' + msg.encode())
    data = client.recv(10240)
    print(data.decode())
client.close()
