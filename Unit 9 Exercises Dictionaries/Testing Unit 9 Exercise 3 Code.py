#Exercise 3: 

#Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

#Enter file name: mbox-short.txt
#{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
#'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
#'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
#'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
#'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
#'ray@media.berkeley.edu': 1}

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

#Code below shows how you can open a file that's not in the same directory as the python file. Basically, you have to specify the file path and separate the folders using /
file_path = ("c:/Users/hlee2/OneDrive/Documents/Python Scripts/Python for Everybody/Unit 7 Exercises/For Unit 7 Exercise.txt")                 
fhand = open(file_path)

contact_dictionary={}
for line in fhand:
    #print (line)
    #Line above to confirm that the file is being read 
    line = line.split() 
    #split the line into a list
    if len(line)>0 and line[0] == 'From': 
        #email_address_check = line[0:2]
        #print (email_address_check)
        #Line above used to confirm that code is picking up email addresses that are sending out emails 
        email_address = line[1]
        contact_dictionary[email_address] = contact_dictionary.get(email_address,0)+1
print (contact_dictionary)
#Confirmed that contact_dictionary contains all the email addresses that sent out emails and the correct counts for each email address 