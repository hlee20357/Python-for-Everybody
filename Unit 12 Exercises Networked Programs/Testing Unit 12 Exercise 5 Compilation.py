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
#user_response_2 = input('Is the URL you want to access a text or an image/jpeg? Acceptable responses are only "Text" or "Image" (without the quotes).')

while True:
    user_response_2 = input('Is the URL you want to access a text or an image/jpeg? Acceptable responses are only "Text" or "Image" (without the quotes). Response: ')
    if user_response_2 != 'Text' and user_response_2 != 'Image':
    #Accessed if the user_response is neither 'Text' or 'Image'  
        print ('You put in the wrong response! Try again. ')
    else: 
        break

#This while loop ensures that you know if you are accessing a text or image. 

try: 
    user_response_for_splitting = user_response.split('/')
    main_website=user_response_for_splitting[2]
    mysock.connect((main_website, 80))
except: 
    print ('This did not work. Sorry!')
    exit()

cmd = 'GET '+ user_response+ ' HTTP/1.0\r\n\r\n'
mysock.sendall(cmd.encode())

if user_response_2 == 'Image': 
    picture  = b""

    count = 0
    while True:
        data = mysock.recv(5000)
        time.sleep(0.25)
        if len(data) < 1:
            break
        count = count +len(data)
        print ('Data received: ', len(data), 'Total data received: ', count)
        #Give a time delay of 0.25 seconds to ensure that every receiving cycle is 1000 characters.
        picture = picture + data
    
    position2 = picture.find(b"\r\n\r\n")
    #This finds the index of the first \r from \r\n\r\n
    #As a result, adding 4 to position 2 leads to the index of the beignning of the picture data. 
    beginning_of_pic_data = position2+4

    #Skips past the header and saves the picture data 
    picture = picture[beginning_of_pic_data: ]
    #No number to the right of the colon means it prints to the very end of the variable. 
    fhand = open("P4E_cover_photo.jpg", "wb")
    #Since writing an image, you have to write (w) in binary (b)
    fhand.write(picture)
    fhand.close()
    #Note: At the end, it makes a jpg with the title that you inputted in your working directory and saves the image data to the jpg. 

if user_response_2 == 'Text': 
    empty_string = ''

    while True:
        data = mysock.recv(1000)
        time.sleep(0.25)
        #Give a time delay of 0.25 seconds to ensure that every receiving cycle is 1000 characters.
        if len(data) < 1:
            break
        x = data.decode()
        empty_string = empty_string + x 
        #append all the converted string data into the empty_string. 
        #By doing it this way, you can access the whole dataset once all the data has been received. 
    position = empty_string.find('\r\n\r\n')
    #This finds the index of the first \r from \r\n\r\n
    #As a result, adding 4 to position leads to the index of the beignning of the text data 
    beginning_of_text = position+4

    print ('')
    print (empty_string[beginning_of_text: ], end = '')
    #No number to the right of the colon means it prints to the very end of the variable. 

#Conclusions 
#While loop made sure you either inputted "Text" or "Image"
#The text data was only printed when tested on http://data.pr4e.org/romeo.txt
#A jpg was created in the directory that I selected when I inputted http://data.pr4e.org/cover3.jpg