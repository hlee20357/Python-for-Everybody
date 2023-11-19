#Exercise 3: 
# 
#Use urllib to replicate the previous exercise of 
# (1) retrieving the document from a URL, 
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