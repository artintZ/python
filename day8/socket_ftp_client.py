# Author: zzk


import socket


client = socket.socket()
client.connect(('localhost', 9999))

while True:
    cmd = input('>>').strip()
    if len(cmd)==0:
        continue
    if cmd.startswith('get'):
        client.send(cmd.encode())
        server_response = client.recv(1024)
        print('server response:',server_response)
        client.send(b'ready to receive file')
        file_size = int(server_response.decode())
        received_size = 0