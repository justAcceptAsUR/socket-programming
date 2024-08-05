import socket
host  = '10.0.2.15'
port = 60000
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    client.connect((host,port))
    while True:
        msg = input('enter message: ')
        client.send(msg.encode())
        res = client.recv(1024).decode()
        if res == 'bye':
            print('bye')
            break
        print(res)
    client.close()