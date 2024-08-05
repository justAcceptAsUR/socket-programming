import socket
import datetime
host = 'localhost'
port = 2000

#create socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind port and address
server.bind((host,port))

#listen and set backlog limit
server.listen(5)

#accept incomming request
newSocket,address = server.accept()


while True:
    request = newSocket.recv(1024).decode()
    today = datetime.datetime.now()
    response = ''
    if request == 'date':
        response = today.strftime('%d %b ,%Y')
    elif request == 'day':
        response = today.strftime("%A")
    elif request == 'time':
        response = today.strftime('%I:%M %p')
    elif request == 'exit':
        newSocket.close()
        server.close()
        break

    newSocket.send(response.encode())








