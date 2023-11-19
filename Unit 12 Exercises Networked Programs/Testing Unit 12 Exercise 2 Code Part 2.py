import socket
import time
HOST = 'data.pr4e.org'
PORT = 80
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect((HOST, PORT))
mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
count = 0
picture = b""

while True:
    data = mysock.recv(3000)
    if len(data) < 1: 
        break
    time.sleep(0.25)
    x = len(data)
    count = count + x
    print(x, count)
    picture = picture + data
    if count <=3000: 
        print (picture)

print ('Total count of characters: ', count)
mysock.close()

#Code works where only 3000 characters are received at a time, and only the first 3000 characters are printed. 