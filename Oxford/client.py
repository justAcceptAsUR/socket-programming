import socket
import json
host = 'localhost'
port = 2000

#create socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#connection request
client.connect((host,port))

while True:
    #start conversation
    query = input('Enter word:')
    if query == 'q':
        break
    client.send(query.encode())

    # #handle response
    response = client.recv(1024)
    data = json.loads(response).decode()
    print(data)

client.close()