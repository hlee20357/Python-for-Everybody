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
#file_path = Path("c:/Users/hlee2/OneDrive/Documents/Python Scripts/Python for Everybody/Unit 7 Exercises/For Unit 7 Exercise.txt")                 
#fhand = open(file_path)

#fhand = open('py4e_code3_romeo.txt')
#for line in fhand: 
#    print (line)

fname = input('Enter file name: ')
#print (fname)
#print (type(fname))
#Note: your input doesn't need to have '' in it because fname is already a string, and you're passing the string into the open function. 

try: 
    fhand = open(fname)
except: 
    print ('File cannot be opened: ', fname)
    exit()
unique_word_list = []
for line in fhand: 
    words_in_lst = line.split()
    for word in words_in_lst: 
        if word not in unique_word_list: 
            unique_word_list.append(word)
unique_word_list.sort()
print ('Sorted unique word list: ', unique_word_list)


    
