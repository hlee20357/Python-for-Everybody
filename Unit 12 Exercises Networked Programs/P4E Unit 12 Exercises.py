#Chapter 12: Networked programs 

#Exercise 1: Change the socket program socket1.py to prompt the user for the URL so it can read any web page. 
#You can use split('/') to break the URL into its component parts so you can extract the host name for the socket connect call. 
#Add error checking using try and except to handle the condition where the user enters an improperly formatted or non-existent URL.

#Original socket1.py below. 

#import socket
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#mysock.send(cmd)
#while True:
#    data = mysock.recv(512)
#    if len(data) < 1:
#        break
#    print(data.decode(),end='')
#mysock.close()

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
mysock.send(cmd.encode())
while True:
    data = mysock.recv(512)
    #At this stage, data that's encoded is of class bytes objects
    #print (data)
    #print ('space')
    if len(data) < 1:
        break
    #print ('  Y           ') used to determine what was happening 
    print(data.decode(),end = '')
    #Note: data.decode() can be saved as a variable 
    #data.decode() class type is a string. 

mysock.close()

#Note. There is a difference between print(data.decode(),end='') and print (data.decode())

#data.decode() leads to 
#...
#Who is already s
#ick and pale with grief
#[blank line]

#data.decode(),end='' leads to 
#...
#Who is already sick and pale with grief
#No blank line here 

#For print, you can have an optional end parameter. 
#It specifies what to print at the end, and the default is a new blank line. 

#Since the text that it is receiving is greater than 512 characters, the 512 characters will be printed and then after that 512th character, a new line will be formed. 
#This can be seen because a new line is formed after "Who is already s" The new line is formed, and the second time the print statement is reached, the printing begins on that new line. 
#That's why if you do end = '' with the print statement, a continuous text is printed because there was no new line to start printing from. 
#with end = '', the printing continues where it left off. 
#Although it seems like all 512 characters went through on the first try, it actually didn't happen. 

#Note: I was able to get http://data.pr4e.org/romeo.txt to be printed with the formated socket1.py with added try/except block and input statement. 

#Exercise 2: 
# 
# Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. 
# The program should retrieve the entire document and count the total number of characters and display the count of the number of characters at the end of the document.

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
mysock.send(cmd.encode())

#The above is a copy and paste from exercise 1. 

count = 0
while True:
    data = mysock.recv(1000)
    time.sleep(0.25)
    #Give a time delay of 0.25 seconds to ensure that every receiving cycle is 1000 characters.
    x = len(data)
    count = count + x
    #print(x, count)
    #Can use this above code to see how many characters you are receiving in one go as well as the total count of characters. 
    if len(data) < 1:
        break
    if count <=3000: 
        print(data.decode(),end='')

print ('Total count of characters: ', count)
mysock.close()

#It seems to have worked with romeo.txt, although that only has ~600 characters, and an altered version of the above code for http://data.pr4e.org/cover3.jpg, which has ~260,000 characters. 

#Exercise 3: 
# 
#Use urllib to replicate the previous exercise of 
# (1) retrievingthe document from a URL, 
#(2) displaying up to 3000 characters, and
#(3) counting the overall number of characters in the document. 
# Don’t worry about the headers for this exercise, simply show the first 3000 characters of the document contents.

import urllib.request, urllib.parse, urllib.error
user_response = input ('Enter the url you want to access: ')
try: 
    fhand = urllib.request.urlopen(user_response)
except: 
    print ('This did not work. Sorry')

count = 0
reverse_count = 3000
for line in fhand: 
    line = line.decode()
    #leads to a string type 
    x= len(line)
    count = count + x
    if count <=3000: 
    #For situations where you won't exceed the 3000 character mark with count 
    #Prompt says you have to display up to 3000 characters. 
    #Based off of the wording, you don't have to display EXACTLY 3000 characters. 
    #For example, if the count before the new line (B) is 2990, and B's length is 30, then any characters in B won't be displayed. 
        print (line, end = '')

print('Character count in the document: ', count)

#Exercise 4: 
# 
# Change the urllinks.py program to extract and count paragraph (p) tags from the retrieved HTML document and display the count of the paragraphs as the output of your program. 
# Do not displayvthe paragraph text, only count them. 
# Test your program on several small web pages as well as some larger web pages.

#Below is what urllinks.py looks like 

# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

#import urllib.request, urllib.parse, urllib.error
#from bs4 import BeautifulSoup
#import ssl

# Ignore SSL certificate errors
#ctx = ssl.create_default_context()
#ctx.check_hostname = False
#ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
#html = urllib.request.urlopen(url, context=ctx).read()
#soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
#tags = soup('a')
#for tag in tags:
#print(tag.get('href', None))









#Exercise 5: (Advanced) 
# Change the socket program so that it only shows data after the headers and a blank line have been received. 
# Remember that recv receives characters (newlines and all), not lines.

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