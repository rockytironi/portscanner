import socket

target = input('Enter IP address to scan: ')
portrange = input('Enter port range to scan: ')

lowport = int(portrange.split('-')[0])
highport = int(portrange.split('-')[1])

print('Scanning host: ', target, 'from port', lowport, 'to port', highport)

for port in range(lowport, highport):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target, port))
    if (status == 0):
        print('*** Port', port, 'OPEN ***')
    else:
        print('Port', port, 'CLOSED')
    s.close()
    
