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
    z = re.findall('java$',line)
    if len(z)>0:
        count = count+1

print (y, ' had ', count, ' lines that mached ', x)

#For ^Author, 1798 lines were counted 
#For ^X-, 14368 lines were counted 
#For java$, I get 4218 lines counted. That is different from what the exercise says it should be. 