from socket import *
import sys

sock = socket(AF_INET,SOCK_DGRAM)
server_address= ('localhost',11000)
sock.bind(server_address)

while True:
	print('Waiting to recieve requests')
	data,addr = sock.recvfrom(4096)
	print('Recieved request: ',data.decode())
	if data:
                ip = "DNS_record_not_found"
                with open('dns.txt') as file:
                        for line in file:
                                domainList = line.split()
                                print(domainList)
                                if domainList[0] == data.decode():
                                        ip = domainList[1]
                        
                print('Sending : ',ip)
                sent = sock.sendto(ip.encode(),addr)
	else:
                print('Sending : "empty"')
                sent = sock.sendto("empty".encode(),addr)
