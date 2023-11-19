#Unit 11 Exercises Regular Expressions 

#Exercise #1 

#Write a simple program to simulate the operation of the grep command on Unix. 
#Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

#$ python grep.py
#Enter a regular expression: ^Author
#mbox.txt had 1798 lines that matched ^Author

#$ python grep.py
#Enter a regular expression: ^Xmbox.
#txt had 14368 lines that matched ^X-

#$ python grep.py
#Enter a regular expression: java$
#mbox.txt had 4175 lines that matched java$

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

file_path = ("C:/Users/hlee2/OneDrive/Documents/Python Scripts/Python for Everybody/Unit 9 Exercises Dictionaries/mbox.txt")
fhand = open (file_path)

def check_if_file_opens(fhand):
    count = 0 
    for line in fhand: 
        print (line)
        count = count + 1
        if count ==10: 
            return (count)

#print (check_if_file_opens(fhand))
import re 

x = input('Enter a regular expression: ')
y = input ('Enter file name that you opened: ')
count = 0 
for line in fhand: 
    line = line.rstrip()
    z = re.findall(x,line)
    if len(z)>0:
        count = count+1

print (y, ' had ', count, ' lines that mached ', x)

#For ^Author, 1798 lines were counted.
#For ^X-, 14368 lines were counted.
#For java$, I get 4218 lines counted. That is different from what the exercise says it should be. 


#Exercise 2

#Write a program to look for lines of the form:

#New Revision: 39772

#Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

#Enter file:mbox.txt
#38549

#Enter file:mbox-short.txt
#39756

#Assume you have to reset your directory (as if starting from scratch)

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

#file_path = ("C:/Users/hlee2/OneDrive/Documents/Python Scripts/Python for Everybody/Unit 9 Exercises Dictionaries/mbox.txt")

file_name = input('Enter file: ')
try: 
    fhand = open (file_name)
except: 
    print ('This file could not be opened.')
    exit()

#def check_if_file_opens(fhand):
#    count = 0 
#    for line in fhand: 
#        print (line)
#        count = count + 1
#        if count ==10: 
#            return (count)

#print (check_if_file_opens(fhand))

import re 

total = 0
counter = 0
for line in fhand: 
    line =line.rstrip() 
    z = re.findall('New Revision:.([0-9]+)', line)
    #Note: I think if you do 'New Revision:.+([0-9]+)' as the regular expression, you are only capturing the last digit in the new revision number. 
    #The .+ means there's one or more wild card characters, so it greedily captures everything. 
    #In doing so, it leaves the parantheses with the last digit in the new revision number. 
    #This is because the parantheses is basically only capturing the last digit it sees in z. 
    #print (z)
    if len(z)>0:
        counter = counter +1 
        number = int(z[0])
        total = total + number
average= int(total/counter)
print (average)

#For mbox.txt, the average is 38549
#For mbox_short.txt, the average is 39756
