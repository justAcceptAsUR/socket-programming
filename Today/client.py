#purpose:
#services: now,date,time,day,month,quit,help
import socket

#remote host config
host = 'localhost'
port = 60000


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    client.connect((host,port))
    #start session
    while True:
        request = input('Enter Query:')
        if request == 'quit':
            break
        client.send(request.encode())
        raw_data = client.recv(1024)
        print(raw_data.decode())
        
    client.close()  

