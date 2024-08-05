import pymongo
import socket
import json
host='localhost'
port = 2000
#connect to mongodb
connectTo = pymongo.MongoClient('mongodb://localhost:27017')
db = connectTo['shaiduck']
oxford = db['oxford']




#create socket 
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#bind host and port
server.bind((host,port))

#listen on connection
server.listen(4)

#accept connection
newSocket,address = server.accept()

#provide service to client
#here: it is dictionary

while True:
    #receive query 
    query = newSocket.recv(1024).decode()
    if query == 'q':
        break
    print(query)

    result = oxford.find_one({"word":query})
    
    newSocket.send(json.dumps(result).encode())

server.close()
newSocket.close()

