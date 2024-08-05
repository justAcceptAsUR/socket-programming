import socket
#defining host and port
localhost = '127.0.0.1'
port=9000

#creating socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connect request
client.connect((localhost,port))

#begin The conversation
data = "hello"

client.send(data.encode())
dataReceived=client.recv(1024).decode()
print(dataReceived)

client.close()







