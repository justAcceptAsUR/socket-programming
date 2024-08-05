import socket

host = 'https://api.dictionaryapi.dev'
port = 443

#creating socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connection request
client.connect((host,port))

data = client.recv(1024)
print(data)




