import socket


localhost = "127.0.0.1"
port = 50000
# create socket

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('socket created\n')


# connect
client_socket.connect((localhost,port))
print('connected\n')


# send & receive information

message = 'Hi from client'

client_socket.send(message.encode())
print('data sended from client\n')

data = client_socket.recv(1024)
print('data received from server\n')

print('message from server:',data.decode())

# close connection
client_socket.close()