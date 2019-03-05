# Author: zzk


import socket

client = socket.socket()
client.connect('localhost', 6969)

client.send('Hello world!')
data = client.recv(1024)
print(data)
client.close()
