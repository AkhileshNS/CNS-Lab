import socket

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientSock.sendto("Hello Server", ("127.0.0.1", 6789))
msg = clientSock.recv(1024)
print("Echo from Server: " + msg)