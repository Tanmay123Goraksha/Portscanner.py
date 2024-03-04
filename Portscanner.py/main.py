import socket
import termcolor








def scan(target,port):
        print('\n' + 'Starting Scan For' +  str(target))
        for port in range(1,ports):
                scan_port(target,port)

















def scan_port(ipaddress,port);
    try:


                sock = socket.socket()
                sock.connect((ipaddress,port))
                print("Port Opened [+]" + str(port))


    except:
                pass














targets = input("Enter Target To Scan(split them by ,)")
ports = int(input("Enter How many Ports You Want TO Scan"))


if ',' in targets:
    printf("Scanning Multiple Targets")
    for ip_addr in targets.split(','):
         scan(ip_addr.stip(''), ports)


else:
    scan(target,ports)
    












