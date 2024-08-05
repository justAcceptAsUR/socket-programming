#queries: now,date,time,day,month,quit
import socket
from datetime import datetime

#server config
host = 'localhost'
port = 60000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind((host,port))
    server.listen(2)
    carrier,address = server.accept()
    #start session
    while True:
        ans = '' 
        query = carrier.recv(1024).decode()
        calender = datetime.today()
        if query == 'date':
            ans = calender.strftime("%d")+'-'+calender.strftime("%m")+'-'+calender.strftime("%Y")
        elif query == 'time':
            ans = calender.strftime("%H:%M %p")
        elif query == 'day':
            ans = calender.strftime("%A")
        elif query == 'month':
            ans = calender.strftime("%B")
        elif query == 'now':
            ans = str(calender)
        elif query == 'help':
            ans = """
            command \t usage\n
            date \t today's date\n
            time \t gives current time\n
            day \t gives weekday name\n
            month \t gives current month name\n
            now \t gives datetime stamp\n
            quit \t for terminating program\n"""
        else:
            ans = """
            no such command permitted\n
            type help for more info
            """
        carrier.send(ans.encode())
        

    carrier.close()  
    server.close()


