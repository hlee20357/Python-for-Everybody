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
