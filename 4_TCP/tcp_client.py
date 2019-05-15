import socket

s = socket.socket()
s.connect(('127.0.0.1', 6789))
s.send('Hello Server')

with open('client.txt', 'wb') as f:
    while True:
        data = s.recv(1024)
        if not data:
            break
        f.write(data)

f.close()
s.close()