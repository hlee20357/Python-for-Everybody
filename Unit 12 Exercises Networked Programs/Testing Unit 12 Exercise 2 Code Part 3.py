import time
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
user_response = input ('Enter a URL you want to read: ')
try: 
    user_response_for_splitting = user_response.split('/')
    main_website=user_response_for_splitting[2]
    mysock.connect((main_website, 80))
except: 
    print ('This did not work. Sorry!')
    exit()

cmd = 'GET '+ user_response+ ' HTTP/1.0\r\n\r\n'
mysock.sendall(cmd.encode())
picture = b""

#The above is a copy and paste from exercise 1. 

count = 0
while True:
    data = mysock.recv(1000)
    time.sleep(0.25)
    #Give a time delay of 0.25 seconds to ensure that every receiving cycle is 1000 characters.
    x = len(data)
    count = count + x
    print(x, count)
    #Can use this above code to see how many characters you are receiving in one go as well as the total count of characters. 
    picture = picture + data
    if len(data) < 1:
        break
    if count <=3000: 
        print (picture)

print ('Total count of characters: ', count)
mysock.close()