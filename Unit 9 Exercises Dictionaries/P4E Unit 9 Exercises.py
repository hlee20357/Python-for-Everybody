#Unit 9: Dictionaries 

#Exercise 1

#Download a copy of the file www.py4e.com/code3/words.txt

#Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
#It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

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
#file_path = ("c:/Users/hlee2/OneDrive/Documents/Python Scripts/Python for Everybody/Unit 7 Exercises/For Unit 7 Exercise.txt")                 
#fhand = open(file_path)


import string 
string.punctuation
fname = 'py4e.com_code3_words.txt' 
fhand = open(fname)
word_dict = {}
for line in fhand: 
    line = line.rstrip()
    #removes any trailing characters (characters at the end of the string aka the line)   
    line = line.translate(line.maketrans('','', string.punctuation))
    #line.translate(str.maketrans(fromstr, tostr, deletestr))
    #Replace the characters in fromstr with the character in the same position in tostr and delete all characters that are in deletestr. 
    # The fromstr and tostr can be empty strings and the deletestr parameter can be omitted.
    #Therefore, you are just deleting all the punctuation that exists in each line. 
    line = line.lower()
    #makes all words be lowercase
    line = line.split()
    #splits a string into a list where each word is a list item 
    #if you didn't have this line and went to the for loop, each character would be printed 
    for word in line: 
        word_dict[word] = word_dict.get(word,0)+1
        #each key (which is the word) has a value that is a counter telling us how many times the word appears in the text. 
print (word_dict)

print ('programs' in word_dict)
#Should output True, and it does! 

#Exercise 2 

#Write a program that categorizes each mail message by which day of the week the commit was done. 
# To do this look for lines that start with “From”, then look for the third word and keep a running count of each of the days of the week. 
# At the end of the program print out the contents of your dictionary (order does not matter).

#Sample Line:
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

#Sample Execution:

#python dow.py
#Enter a file name: mbox-short.txt
#{'Fri': 20, 'Thu': 6, 'Sat': 1}

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

day_counter={}
for line in fhand: 
    line = line.split()
    if len(line)>0 and line[0] == 'From': 
        day_of_the_week = line[2]
        #print (day_of_the_week)
        #Checking if I'm getting the day of the week from the line
        day_counter[day_of_the_week] = day_counter.get(day_of_the_week,0)+1
print (day_counter)
#Confirmed to print out dictionary as {'Sat': 1, 'Fri': 20, and 'Thu': 6}

#Exercise 3: 

#Write a program to read through a mail log, build a histogram using a dictionary to count how many messages have come from each email address, and print the dictionary.

#Enter file name: mbox-short.txt
#{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
#'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
#'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
#'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
#'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
#'ray@media.berkeley.edu': 1}

#Although Exercise 2 has all the import os...etc code, assume that the exercise starts from a fresh block of code. 

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

#Exercise 4 

# Add code to the above program to figure out who has the most messages in the file. 
# After all the data has been read and the dictionary has been created, look through the dictionary using a maximum loop (see Chapter 5: Maximum and minimum loops) to find who has the most messages and print how many messages the person has.

#Enter a file name: mbox_short.txt
#cwen@iupui.edu 5

#Enter a file name: mbox.txt
#zqian@umich.edu 195

#Although Exercise 2 has all the import os...etc code, assume that the exercise starts from a fresh block of code. 

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
email_address_dictionary = {}
for line in fhand: 
    #print (line)
    #counter = counter +1
    #if counter ==10:
    #    break
    #Lines above are used to confirm that I can read the file. 
    line = line.split() 
    if len(line) >0 and line[0] == 'From': 
        email_address = line[1]
        email_address_dictionary[email_address] = email_address_dictionary.get(email_address,0) + 1

x = max(email_address_dictionary.values())
#print (x)

for key in email_address_dictionary: 
    if email_address_dictionary[key] == x: 
        most_messages_sent = key 
print (most_messages_sent, x)
#Confirmed that the print statement (print (most_messages_sent, x)) does indeed print out (zqian@umich.edu 195) for mbox.txt and (cwen@iupui.edu 5) for mbox_short.txt

#Exercise 5
# 
# This program records the domain name (instead of the address) where the message was sent from instead of who the mail came from (i.e., the whole email address). 
# At the end of the program, print out the contents of your dictionary.

#python schoolcount.py
#Enter a file name: mbox-short.txt
#{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
#'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

#Although Exercise 2 has all the import os...etc code, assume that the exercise starts from a fresh block of code. 

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
        start_of_domain = email_address.find('@')
        #provides the index where @ is found in integer form
        email_address_length = len(line[1])
        domain = email_address[(start_of_domain)+1: email_address_length]
        email_domain_name_dictionary[domain] = email_domain_name_dictionary.get(domain,0)+1
print (email_domain_name_dictionary)

#Note: Instead of using start_of_domain = email_address.find('@'), you can use a tuple to split the email address into username and domain. 
#Code below would output the same results as the block of code above from Lines 302 to 317 

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