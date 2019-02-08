# Author: zzk

msg = "王者荣耀"
print(msg.encode())  # encode()默认对utf-8编码成bytes类型
print(msg.encode().decode())  # decode()默认对bytes类型解码为utf-8