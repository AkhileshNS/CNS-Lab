from socket import *
import sys

sock = socket(AF_INET,SOCK_DGRAM)
server_address = ('localhost',11000)

try:
	while True:
		msg = input('Enter domain name: ')
		print('Sending request for : ',msg)
		sent = sock.sendto(msg.encode(),server_address)
		print('Waiting to recieve to recieve ip')
		l,addr = sock.recvfrom(4096)
		print('Recieved : ',l.decode())
finally:
	print('closing socket')
	sock.close()
