# Client


from socket import *

HOST = 'localhost'
PORT = 5001
address = '127.0.0.1'


s = socket(AF_INET, SOCK_STREAM)
s.connect((address, 1234))  # You should set these.
s.send(b'Hello, world!')
data = s.recv(1024)
print(data)
print(f"hello")
s.close()



