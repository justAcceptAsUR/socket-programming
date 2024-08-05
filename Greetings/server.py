import socket

localhost='127.0.0.1'
port = 50000
#create server socket
server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('server socket created\n')

#bind address & port
server_socket.bind((localhost,port))
print('address binded to port\n')

#listen on port
server_socket.listen(5)
print('socket is listening\n')

#accept connection
client_socket,client_address = server_socket.accept()
print('connected\n')

data = client_socket.recv(1024)
print('data received from client\n')

client_socket.send(data)
print('data back to client\n')

server_socket.close()
client_socket.close()