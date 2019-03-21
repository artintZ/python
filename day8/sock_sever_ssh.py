# Author: zzk


import os
import socket

server = socket.socket()
server.bind(('localhost', 9999))
print('server starts')
server.listen()
while True:
    conn, addr = server.accept()
    print('new connection', addr)
    while True:
        data = conn.recv(1024)
        if not data:
            print('Client has lost...')
            break
        print('execution command: ', data)
        cmd_res = os.popen(data.decode()).read()
        if len(cmd_res) ==0:
            cmd_res = 'cmd has no output'
        conn.send(str(len(cmd_res.encode())).encode())
        client_res = conn.recv(1024)
        print(client_res)
        conn.send(cmd_res.encode())

server.close()
