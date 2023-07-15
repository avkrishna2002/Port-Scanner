from ipaddress import ip_address
import socket
from IPy import IP


def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)


ipaddress = input('[+] Enter the ip adress:')
converted_ip=check_ip(ipaddress)

def scan_port (ipaddress, port):


    try:

        sock = socket.socket()
        sock.settimeout(1)
        sock.connect((ipaddress,port))
        print('[+] port' + str(port) + 'is open')


    except:
            print('[-] port' + str(port) + 'is closed')


for port in range (20,100):
    scan_port(converted_ip,port)

