#Exercise 5
# 
# This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). 
# At the end of the program, print out the contents of your dictionary.

#python schoolcount.py
#Enter a file name: mbox-short.txt
#{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
#'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

import os 
#from pathlib import Path
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

fname = input('Enter file name: ')
#Note: your input doesn't need to have '' in it because fname is already a string, and you're passing the string into the open function. 
#If you add '' to the input, '' wil be part of the string. The file won't be recognized because there aren't '' in the file name. 

try: 
    fhand = open(fname)
except: 
    print ('File cannot be opened: ', fname)
    exit()
try: 
    fhand = open(fname)
except: 
    print ('File cannot be opened: ', fname)
    exit()

#counter = 0
email_domain_name_dictionary = {}
for line in fhand: 
    #print (line)
    #counter = counter +1
    #if counter ==10:
    #    break
    #Lines above are used to confirm that I can read the file. 
    line = line.split() 
    if len(line)>0 and line[0] == 'From': 
        email_address = line[1]
        uname, domain = email_address.split('@')
        email_domain_name_dictionary[domain] = email_domain_name_dictionary.get(domain,0)+1
        #Note: Can also use a tuple of uname, domain = email_address.split(@). 
        #As a result, uname will contain everything before @ and the domain will contain everything afterwards 
print (email_domain_name_dictionary)