import socket

s = socket.socket()
s.bind(('127.0.0.1', 6789))
s.listen(5)

print("Server listening...")
while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    print('Got connection from ' + addr[0] + ": Received " + repr(data))

    f = open('server.txt','rb')
    fileData = f.read(1024)
    while fileData:
        conn.send(fileData)
        fileData = f.read(1024)
    f.close()

    conn.close()
