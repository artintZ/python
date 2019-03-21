# Author: zzk


'''socket.socket()
family address:
    socket.AF_INET  # ipv4
    socket.AF_INET6  # ipv6
    socket.AF_UNIX  # local
socket protocol type:
    socket.SOCK_STREAM  # tcp/ip
    socket.SOCK_DGRAM  # 数据报UDP
    '''

import socket

# server
server = socket.socket()
server.bind(('localhost', 9999))
server.listen()

while True:

    conn, addr = server.accept()  # 阻塞

    while True:
        print('new connection: ', addr)
        data = conn.recv(1024)
        if not data:
            print('Client has lost...')
            break
        print(data)
        conn.send(data.upper())


# client
client = socket.socket()
client.connect(('localhost', 9999))
client.send()
client.send()
client.recv()
