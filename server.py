# Server


with open('./filename.txt', 'r') as f:
    data = f.read()
    print(data)

from socket import *

HOST = 'localhost'
PORT = 5001
address = '127.0.0.1'





s = socket(AF_INET, SOCK_STREAM)
s.bind((address, 1234))  # You should set these.
s.listen(1)
(conn, addr) = s.accept()
while True:

    data = conn.recv(1024)
    print(f"Connection from {address} has been established.")
    if not data:
        break
    print(data)
    conn.send(data)
conn.close()

'''
import socket

address2 = '127.0.0.1'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((address2, 1234))
s.listen(5)

while True:
    # now our endpoint knows about the OTHER endpoint.
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established.")
    '''