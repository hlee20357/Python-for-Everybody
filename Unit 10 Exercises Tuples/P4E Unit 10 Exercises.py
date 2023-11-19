#Unit 10: Tuples

#Exercise 1: 

#Revise a previous program as follows: 
#Read and parse the “From” lines and pull out the addresses from the line. 
#Count the number of messages from each person using a dictionary.
#After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. 
#Then sort the list in reverse order and print out the person who has the most commits.

#Sample Line:

#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5

#Enter a file name: mbox.txt
#zqian@umich.edu 195

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

fname = input('Enter file name: ')
try: 
    fhand = open(fname)
except: 
    print ('File cannot be opened.')

#count = 0
#for line in fhand: 
#    print (line)
#    count = count +1
#    if count ==10: 
#        exit()
#Above code used to verify if the text was opened correctly and is printing out the right text. 

email_dictionary = {}
for line in fhand: 
    line = line.split() 
    #splits a string into a list where each word is a list item 
    #print (line)
    if len(line)>0 and line[0] == 'From': 
        email_address = line[1]
        email_dictionary[email_address] = email_dictionary.get(email_address,0) + 1
print (email_dictionary)
#Above makes the email_dictionary with the keys as the email addresses and the value as the counter for how many times the email address was used to send an email. 

email_list = []
#Note: can do [] to indicate empty list or list() to indicate empty list. 
for key,value in list(email_dictionary.items()): 
    email_list.append((value,key))
#print (email_list)
#make a list made up of tuples where the order is value,key

email_list.sort(reverse = True)
#Sort the list in descending order in respect to the counter. 

print (email_list)
value,email = email_list[0]
#Assign the first index (which is a tuple) of the sorted email_list to value, email. That means the first value in the tuple pair is assigned to variable value, and the second value in the tuple pair is assigned to variable email. 
print (email,value)
#print the correct order 

#cwen@iupui.edu 5 printed out for mbox_short.txt
#zqian@umich.edu 195 printed out for mbox.txt 
#The correct outputs are printed. 

#Exercise 2: 

#This program counts the distribution of the hour of the day for each of the messages. 
# You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. 
# Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

#python timeofday.py
#Enter a file name: mbox-short.txt

#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1

#We are assuming we have to set up the working directory. 

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

fname = input('Enter file name: ')
try: 
    fhand = open(fname)
except: 
    print ('File cannot be opened.')

#count = 0
#for line in fhand: 
#    print (line)
#    count = count +1
#    if count ==10: 
#        exit()
#Above code used to verify if the text was opened correctly and is printing out the right text. 

time_dictionary = {}
for line in fhand: 
    line = line.split() 
    if len(line)>0 and line[0] == 'From':
        time = line[5]
        time_splt = time.split(':')
        hour = time_splt[0]
        time_dictionary[hour] = time_dictionary.get(hour,0)+1
#print (time_dictionary)

time_tuple_list = []
list_time_dictionary = list(time_dictionary.items())
for key,value in list_time_dictionary: 
    time_tuple_list.append((key,value))
    #(value,key) has to be in parantheses because append only takes one argument.
    #Basically, you are appending the key, value as a pair, and the pair becomes an index. 

time_tuple_list.sort()
#print (time_tuple_list)

for key,value in time_tuple_list: 
    print (key,value)

#Confirmed to print out the output stated in the beginning of the exercise. 

#Exercise 3 

# Write a program that reads a file and prints the letters in decreasing order of frequency. 
# Your program should convert all the input to lower case and only count the letters a-z. 
# Your program should not count spaces, digits, punctuation, or anything other than the letters a-z. 
# Find text samples from several different languages and see how letter frequency varies between languages. 
# Compare your results with the tables at https://wikipedia.org/wiki/Letter_frequencies.

#Note: I didn't test it on a text file, but I tested it on a string. 

import string
print (string.digits)
print (string.punctuation)

test_string = 'HI! 1234. This tests whether493! CoDe eliminates DIGITS, PuNcTuATiOn, SP4CE1S, and makes everything LOWERCASE!' 
count_dictionary= {}
x = test_string.lower()
x = x.replace(' ','')
x = x.translate(str.maketrans('','',string.punctuation)) 
x = x.translate(str.maketrans('','',string.digits))
#Above four lines make everything lowercase and gets rid of spaces, punctuation, and digits. 
#print (x)
#To test if everything was lowercased and all the spices, punctuation, and digits were eliminated. 

for char in x:
    count_dictionary[char] = count_dictionary.get(char,0)+1
    #form count_dictionary storing the letters as keys and the values as the counts for each character present in the string. 

total = sum(count_dictionary.values())
#print (total)
#Determine how many characters are in the string. 

for key in count_dictionary: 
    count_dictionary[key] = round((count_dictionary[key]/total)*100,3)
    #update the count_dictionary's values so that they are frequencies of the letter (# of letters in the string/total letters in the string)
    #The values are in percentages rounded to the third decimal point. 

#print (count_dictionary)
#Check if it looks right. 

count_dictionary_list = []
for key,value in list(count_dictionary.items()): 
    count_dictionary_list.append((key,value))
    #Make a list from the count_dictionary so that you can sort it in the future
    
count_dictionary_list.sort()
#Sort in alphabetical order 

print (count_dictionary_list)