import socket
host = 'localhost'
port = 62000

def is_palindrome(num):
    ans = 1
    n = len(num)
    i = 0
    j = n-1
    while i<=j:
        if num[i]==num[j]:
            i = i+1
            j = j-1
            continue
        else:
            ans=0
            break
    return ans

def count_digit(num):
    return len(num)

def check_sign(num):
    x = int(num)
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind((host,port))
    server.listen(5)
    carrier,client_address = server.accept()
    print('server: i am listening')
    while True:
        query =carrier.recv(1024).decode()
        if query=='Thanks':
            carrier.send('your welcome'.encode())
            break
        else:
            ans = ''
            arr = query.split(sep=' ')
            if len(arr) != 2:
                ans = 'invalid query'
            else:
                option = arr[0]
                number = arr[1]
                if option=='cp':
                    ans = is_palindrome(number)
                elif option=='cd':
                    ans = count_digit(number)
                elif option=='cs':
                    ans = check_sign(number)
                else:
                    ans = 'invalid query'
                
            carrier.send(str(ans).encode())



    carrier.close()
    server.close()

