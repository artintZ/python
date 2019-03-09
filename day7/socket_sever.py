# Author: zzk


import socket

sever = socket.socket()
sever.bind(('localhost', 6969))  # 绑定要监听端口
sever.listen(5)  # 监听
print('服务器已开启')
while True:
    conn, addr = sever.accept()
    print(conn, addr)
    # print('电话来了')
    cnt = 0
    while True:
        data = conn.recv(1024)
        print(data.decode())
        if not data:
            # continue
            print('Client has lost...')
            break
        msg = input().strip()
        conn.send(b'sever:' + msg.encode())
        cnt += 1
        if cnt > 9:
            break

sever.close()
