import socket
from datetime import datetime
host = 'localhost'
port = 20000
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind((host,port))
    server.listen(5)
    carrier,client_address = server.accept()
    now = datetime.now()
    while True:
        res = ''
        query = carrier.recv(1024).decode()
        if query == 'quit':
            carrier.send('Bye'.encode())
            break
        elif query == 'date':
            res = now.strftime("%Y-%m-%d")
        elif query == 'time':
            res = now.strftime("%H:%M %p")
        elif query == 'dts':
            res = str(now)
        carrier.send(res.encode())

    carrier.close()
    server.close()
