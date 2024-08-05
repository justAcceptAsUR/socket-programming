#can request: date,time,datetime stamp(dts),quit
import socket
host = 'localhost'
port = 20000
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    client.connect((host,port))
    while True:
        query = input('Enter Your Query:')
        client.send(query.encode())
        res = client.recv(1024).decode()
        if res == 'Bye':
            break
        
        print(res)
    client.close()

