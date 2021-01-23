from IPy import IP
import socket
import sys

s = socket.socket()

ip = input("enter target ip to scan: ")
#port = 53



def port_scan(ip,port):
	try :
		s = socket.socket()
		s.settimeout(0.5)
		s.connect((ip,port))
		print('[+]  {} is open'.format(port))
	except KeyboardInterrupt:
		sys.exit()
	except:

		print('[-] port {} is not open'.format(port))
	 	
for i in range(80):	
	port_scan(ip,port=i)

