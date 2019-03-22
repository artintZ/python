# Author: zzk


import socket
import hashlib


client = socket.socket()
client.connect(('localhost', 9999))

while True:
    cmd = input('>>').strip()
    if len(cmd) == 0:
        continue
    if cmd.startswith('get'):
        client.send(cmd.encode())
        server_response = client.recv(1024)
        print('server response:', server_response)
        client.send(b'ready to receive file')
        file_size = int(server_response.decode())
        if file_size == 0:
            print('No such file!')
            continue
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename+'-new', 'wb')
        m = hashlib.md5()
        while received_size < file_size:
            if file_size - received_size >= 1024:
                size = 1024
            else:
                size = file_size-received_size
                print('the last data size:', size)
            data = client.recv(size)
            m.update(data)
            received_size += len(data)
            f.write(data)
            print(received_size, file_size)
        else:
            new_file_md5 = m.hexdigest()
            print('file receiced done', received_size, file_size)
            f.close()
        server_file_md5 = client.recv(1024).decode()
        print('server file md5:', server_file_md5)
        print('client file md5:', new_file_md5)
client.close()