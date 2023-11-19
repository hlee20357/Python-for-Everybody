#Testing Unit 11 Exercise 2 code 

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