from socket import *  
HOST='128.199.190.36'  
PORT=37695
BUFSIZ=1024  
ADDR=(HOST,PORT)  
tcpCliSock=socket(AF_INET,SOCK_STREAM)  
tcpCliSock.connect(ADDR)  
while True:  
    data=raw_input('>')
    if data == "login":
        name = raw_input("your name : ")
        password = raw_input("password : ")
        print name
        print password
        tcpCliSock.send('%s %s %s'%(data , name , password)) 
        data=tcpCliSock.recv(BUFSIZ)  
        if not data:  
            print"error in receiving"  
        print data
    else:
        if not data:  
            break  
        tcpCliSock.send(data)  
        data=tcpCliSock.recv(BUFSIZ)  
        if not data:  
            print"error in receiving"  
        print data  
tcpCliSock.close()  
