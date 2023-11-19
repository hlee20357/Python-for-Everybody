import time
import socket
import os 
print ('Get current working directory: ', os.getcwd())

print ('For current directory that the script is being run: ', os.path.dirname(os.path.abspath(__file__)))

#In Python, you can use __file__ to get the path of the current file, i.e., the currently running script file (.py). 
# This is particularly useful when you need to read other files relative to the current file's location.
print('basename:    ', os.path.basename(__file__))
#Gives the python file name 
print('dirname:     ', os.path.dirname(__file__))
#Gives the path to which the python file is stored 

#Difference between absolute and relative paths
#Absolute paths give all the \ marks. Relative paths don't. 
#When you do __file__, the absolute path is given for Python 3.9 and above. 

#Note: If you want to read a file, you have to change your working directory to where the file is being stored. 
print('[change directory]')
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print ('')
print('getcwd:      ', os.getcwd())
print('')

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
picture  = b""

#The above is a copy and paste from exercise 1. 

count = 0
while True:
    data = mysock.recv(5000)
    time.sleep(0.25)
    if len(data) < 1:
        break
    count = count +len(data)
    print (len(data), count)
    #Give a time delay of 0.25 seconds to ensure that every receiving cycle is 1000 characters.
    picture = picture + data

position = picture.find(b"image/jpeg")
position2 = picture.find(b"\r\n\r\n")
print (position)
print (position +10+4)
print ('BLANK')
print ('This is position 2', position2)
print (position2 + 4)
x = (picture[0:398].decode())
#Goes from indices 0 to 397. That is why x works. 
#Note: position and position 2 print out 398. In this case, index 398 is the beginning of the picture data. 
print (x, end = '')
#y = picture[398:len(picture)].decode()
#print (y)
#Thus, when you try to act on the y variable, it doesn't work. y is trying to decode index 398 and beyond. 
#You can't decode picture data. 



#print (test)
#print (type(test))
#y = empty_string.find('image/jpeg')
#end_of_headers_and_blank_line = y +len('text/plain')+4
#print (end_of_headers_and_blank_line)
#print (empty_string[0:end_of_headers_and_blank_line])
#print ('BLANK')
#print (empty_string[end_of_headers_and_blank_line:len(empty_string)], end = '')

mysock.close()