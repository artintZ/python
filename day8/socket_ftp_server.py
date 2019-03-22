# Author: zzk


# ftp server
'''
1. 读取文件名
2. 检测文件是否存在
3. 打开文件
4. 检测文件大小
5. 发送文件大小给客户端
6. 等客户端确认
7. 开始边读边发数据
8. 发送MD5
'''

import os
import socket
import hashlib


server = socket.socket()
server.bind(('localhost', 9999))
print('FTP server is runing...')
server.listen()

while True:
    conn, addr = server.accept()
    print('new conn:', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print('Client has lost...')
            break

        cmd, filename = data.decode().split()
        print('filename:', filename)
        if os.path.isfile(filename):
            f = open(filename, 'rb')
            m = hashlib.md5()
            file_size = os.stat(filename).st_size
            conn.send(str(file_size).encode())
            conn.recv(1024)
            for line in f:
                m.update(line)
                conn.send(line)
            print('file md5:', m.hexdigest())
            f.close()
            conn.send(m.hexdigest().encode())
            print('send done')
        else:
            conn.send(b'0')

server.close()
