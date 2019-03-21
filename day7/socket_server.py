# Author: zzk


import socket

server = socket.socket()
server.bind(('localhost', 6969))  # 绑定要监听端口
server.listen(5)  # 监听
print('服务器已开启')
while True:
    conn, addr = server.accept()
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
        conn.send(b'server:' + msg.encode())
        cnt += 1
        if cnt > 9:
            break

server.close()
