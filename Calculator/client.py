#calculator: addition,substraction,division,multiplication
import socket
host='localhost'
port=6000
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    client.connect((host,port))
    while True:
        query = input('Enter Expression: ')
        client.send(query.encode())
        res = client.recv(1024).decode()
        print(res)
        if res=='welcome':
            break
        
    client.close()     