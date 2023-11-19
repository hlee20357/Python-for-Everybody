#Exercise 1

#Write a function called chop that takes a list and modifies
#it, removing the first and last elements, and returns None. Then write
#a function called middle that takes a list and returns a new list that
#contains all but the first and last elements.

def chop(x): 
    length = len(x)
    x.pop(length-1)
    x.pop(0)

test_list = ['a', 'b','c', 'd']
chop(test_list)
print(test_list)
print(chop(test_list))

def middle(y): 
    new_list = y
    length = len(new_list)
    del new_list[length-1]
    del new_list[0]
    return new_list 
    
test_list_2 = ['A', 'B', 'C', 'D']
print (middle(test_list_2))


#Exercise 2
# Figure out which line of the above program is still not properly guarded. 
# See if you can construct a text file which causes the program to fail and then modify the program so that the line is properly guarded and test it to make sure it handles your new text file.

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

fhand = open('For Unit 7 Exercise.txt')
days = ['Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
for line in fhand:
    words = line.split()
    #.split() splits a string into a list. If no separator is specified, then the string will split into a list based off of the white spaces. 
    #Therefore, each word in the string is an index in the new list. 
    if len(words) > 0 and words[0] == 'From' and any(item in words for item in days):
    #checks if the list words has greater than 0 elements 
    #checks if the first element in the list words is "From"
    #checks if any words in the lowercase string are one of the elements in the list days. Outputs a true or false statement. 
    #If true for all, then you move forward. 
        for written_days in days: 
        #for loop to go through each element in days list. written_days is the iterating variable. 
            if written_days in words: 
            #if the current element is in the list, print the current element 
                print (written_days) 
                continue
                #once the print statement is executed, you can move on to the next line because there is only one written_day in the specific line. 



#Exercise 3: 
#Rewrite the guardian code in the above example without two if statements. 
# Instead, use a compound logical expression using the or logical operator with a single if statement.

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
#file_path = ("c:/Users/hlee2/OneDrive/Documents/Python Scripts/Python for Everybody/Unit 7 Exercises/For Unit 7 Exercise.txt")                 
#fhand = open(file_path)

fhand = open('For Unit 7 Exercise.txt')
count = 0
for line in fhand:
    words = line.split()
# print('Debug:', words)
    if len(words) == 0 or words[0] != 'From':
        continue
    print(words[2])


#Exercise 4: 
# Find all unique words in a file 
# 
# Shakespeare used over 20,000 words in his works. 
# But how would you  determine that? How would you produce the list of all the words that Shakespeare used? 
# Would you download all his work, read it and track all unique words by hand?
#Let’s use Python to achieve that instead. List all unique words, sorted in alphabetical order, that are stored in a file romeo.txt containing a subset of Shakespeare’s work.

#To get started, download a copy of the file www.py4e.com/code3/romeo.txt.
#Create a list of unique words, which will contain the final result. 
# Write a program to open the file romeo.txt and read it line by line. 
# For each line, split the line into a list of words using the split function. 
# For each word, check to see if the word is already in the list of unique words. 
# If the word is not in the list of unique words, add it to the list.
#When the program completes, sort and print the list of unique words in alphabetical order.
#Enter file: romeo.txt
#['Arise', 'But', 'It', 'Juliet', 'Who', 'already',
#'and', 'breaks', 'east', 'envious', 'fair', 'grief',
#'is', 'kill', 'light', 'moon', 'pale', 'sick', 'soft',
#'sun', 'the', 'through', 'what', 'window',
#'with', 'yonder']

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
#file_path = ("c:/Users/hlee2/OneDrive/Documents/Python Scripts/Python for Everybody/Unit 7 Exercises/For Unit 7 Exercise.txt")                 
#fhand = open(file_path)

#fhand = open('py4e_code3_romeo.txt')
#for line in fhand: 
#    print (line)

fname = input('Enter file name: ')
#Note: your input doesn't need to have '' in it because fname is already a string, and you're passing the string into the open function. 
#If you add '' to the input, '' wil be part of the string. The file won't be recognized because there aren't '' in the file name. 

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


#Exercise 5: Minimalist Email Client

#MBOX (mail box) is a popular file format to store and share a collection of emails. This was used by early email servers and desktop apps.
#Without getting into too many details, MBOX is a text file, which stores emails consecutively. 
# Emails are separated by a special line which starts with From (notice the space). 
# Importantly, lines starting with From: (notice the colon) describes the email itself and does not act as a separator. 
# Imagine you wrote a minimalist email app, that lists the email of the senders in the user’s Inbox and counts the number of emails.

#Write a program to read through the mail box data and when you find line that starts with “From”, you will split the line into words using the split function. 
# We are interested in who sent the message, which is the second word on the From line.

#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

#You will parse the From line and print out the second word for each From line, 
# then you will also count the number of From (not From:) lines and print out a count at the end. 
#
# This is a good sample output with a few lines removed:

#python fromcount.py
#Enter a file name: mbox-short.txt
#stephen.marquard@uct.ac.za
#louis@media.berkeley.edu
#zqian@umich.edu
#[...some output removed...]
#ray@media.berkeley.edu
#cwen@iupui.edu
#cwen@iupui.edu
#cwen@iupui.edu
#There were 27 lines in the file with From as the first word

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

fhand = open('For Unit 7 Exercise.txt')
count = 0 
email_lst = []
for line in fhand:
    words = line.split()
#   print (words) to check if it's printing right 
    if len(words) > 0 and words[0] == 'From': 
        email_address = words[1]
        email_lst.append(email_address)
        count = count +1
print (email_lst)
print ('There were ', count, ' lines in the file with From as the first word.')

#Exercise 6

R#ewrite the program that prompts the user for a list of umbers and prints out the maximum and minimum of the numbers at the end when the user enters “done”. 
#Write the program to store the numbers the user enters in a list and use the max() and min() functions to compute the maximum and minimum numbers after the loop completes.
#Enter a number: 6
#Enter a number: 2
#Enter a number: 9
#Enter a number: 3
#Enter a number: 5
#Enter a number: done
#Maximum: 9.0
#Minimum: 2.0

num_lst = []
while (True): 
    inp = input('Enter a number: ')
    if inp == 'done':
        break
        #escapes the while loop 
    try: 
        value = float(inp)
        #try to make the input into a float. 
        #Sometimes, inputs may be non float or integer numbers. 
        #If it happens, the except code is executed. 
    except: 
        print ('This is not a number!')
    num_lst.append(value)

highest_number = max(num_lst)
lowest_number = min(num_lst)
print ('Maximum: ', highest_number)
print ('Minimum: ', lowest_number)
