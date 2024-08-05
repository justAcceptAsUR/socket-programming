import socket

#define remote host
host = 'localhost'
port = 60000

#create socket
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client_socket:

    #send connection request
    client_socket.connect((host,port))

    while True:
        #start conversations
        msg = input('Enter your message:')
        client_socket.send(msg.encode())
        raw_data = client_socket.recv(1024)
        data = raw_data.decode()
        print(data,sep='\n')
        if data == 'Bye':
            break

    client_socket.close()       