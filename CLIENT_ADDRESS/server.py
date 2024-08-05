import socket

localhost = '127.0.0.1'
port = 9000

#create socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#binding 
server.bind((localhost,port))

#start listening 
server.listen()

#accept connection on new socket
newSocket,clientAdress = server.accept()
print(clientAdress)

#use newSocket for further communication with client
receivedData = newSocket.recv(1024).decode()
print(f'server received <{receivedData}> from client')
newSocket.send(receivedData.encode())

newSocket.close()
server.close()


