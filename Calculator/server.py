import socket
host='localhost'
port=6000
with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind((host,port))
    server.listen(5)
    carrier,client_address = server.accept()
    while True:
        query=carrier.recv(1024).decode()
        if query=='thanks':
            carrier.send('welcome'.encode())
            break
        else:
            items = query.split(sep=' ')
            if len(items)!=3:
                carrier.send('invalid query'.encode())
                
            else:
                ans = 0
                num1 = int(items[0])
                num2 = int(items[2])
                op = items[1]
                if op=='+':
                    ans = num1+num2
                elif op=='-':
                    ans = num1-num2
                elif op=='*':
                    ans = num1*num2
                elif op=='/':
                    ans = num1/num2
                carrier.send(str(ans).encode())
    
    carrier.close()
    server.close()
                    

