from socket import *
import sys

sock = socket(AF_INET,SOCK_DGRAM)
server_address = ('localhost',11000)

try:
	while True:
		msg = input('Enter domain name (in lowercase letters): ')
		print('Sending request for : ',msg)
		sent = sock.sendto(msg.encode(),server_address)
		print('Waiting to receive ip')
		l,addr = sock.recvfrom(4096)
		print('Received : ',l.decode())
finally:
	print('closing socket')
	sock.close()

# Enter domain name (in lowercase letters): google.com
# Sending request for : google.com
# Waiting to receive
# Received : 8.8.8.8