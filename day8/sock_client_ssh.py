# Author: zzk


import socket

client = socket.socket()
client.connect(('127.0.0.1', 9999))
while True:
    cmd = input('>>').strip()
    if len(cmd) == 0:
        continue
    client.send(cmd.encode())
    cmd_res_size = client.recv(1024)
    print('the data size is', cmd_res_size)
    client.send(b'client prepares done')
    received_size = 0
    received_data = b''
    while received_size < int(cmd_res_size.decode()):
        cmd_res = client.recv(1024)
        received_size += len(cmd_res)
        received_data += cmd_res
    else:
        print('receive done...', received_size)
        print(received_data.decode())

client.close()
