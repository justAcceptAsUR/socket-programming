import socket

host='localhost'
port=2000

#create socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connection request
client.connect((host,port))
while True:
    query = input('Enter Query: ')
    client.send(query.encode())
    if query == 'exit':
        break
    response = client.recv(1024).decode()
    print(response)


