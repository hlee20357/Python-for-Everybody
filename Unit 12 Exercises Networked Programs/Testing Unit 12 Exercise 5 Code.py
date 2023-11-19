#Exercise 5 Unit 12 for documents 

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
#.send() returns the number of bytes sent.
#.sendall() continues to receive data until all data has been sent and returns None. 


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

#Note: Find() finds the FIRST OCCURENCE (AKA the index) of it happening, 
#print (test)
#print (type(test))
y = empty_string.find('text/plain')
print ('This is y:', y)
#This finds the index of t in 'text/plain'. Output is 355. 
very_beginning_of_desired_text = y +len('text/plain')+4
#The +4 comes from sending \r\n\r\n as well as the beginning of the text. 
#adding len('text/plain) is double counting the t in text/plain. That's why the output is 369. 
#Index 369 is actually the beginning of the desired text. 
#Index 368 is the head of all the headers. 
print (very_beginning_of_desired_text, end = '')
#Index 369 is the beginning of the text. 
print (empty_string[0:very_beginning_of_desired_text], end = '')
#This goes from indicies 0 to 368. The number after : is not included. 
print ('BLANK')
print (empty_string[very_beginning_of_desired_text:len(empty_string)], end = '')
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