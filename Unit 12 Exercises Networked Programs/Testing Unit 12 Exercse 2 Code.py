#Exercise 2: 
# 
# Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. 
# The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

import time 
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
count = 0 
while True:
    data = mysock.recv(1000)
    time.sleep(0.25)
    #Give a time delay of 0.25 seconds to ensure that every receiving cycle is 1000 characters.
    x = len(data)
    count = count + x
    #print(len(data), count)
    #Can use this above code to see how many characters you are receiving in one go as well as the total count of characters. 
    if len(data) < 1:
        break
    if count <=3000: 
        print(data.decode(),end='')

print ('Total count of characters: ', count)
mysock.close()