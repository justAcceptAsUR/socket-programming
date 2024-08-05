import socket

#host config
host = 'localhost'
port = 60000

#create server socket 
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server_socket:

    #bind them
    server_socket.bind((host,port))

    #listen
    server_socket.listen(2)

    #the messenger
    messenger,address = server_socket.accept()
    messenger.send(str(address).encode())



    while True:
        #start conversations
        raw_data = messenger.recv(1024)
        data = raw_data.decode()
        if data == 'quit':
            break
        messenger.send(raw_data)

    msg = 'Bye'
    raw_data = msg.encode()
    messenger.send(raw_data)
    messenger.close()
    server_socket.close()
