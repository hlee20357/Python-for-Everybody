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

#fhand = open('For Unit 7 Exercise.txt')
#count = 0
days = ['Mon', 'Tues', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
#for line in fhand:
#    words = line.split()
#    print('Debug:', words)
#    if len(words) > 0 and words[0] == 'From':
#        if any(item in words for item in days):
#                for written_days in days: 
#        #for loop to go through each element in days list. written_days is the iterating variable. 
#                    if written_days in words: 
#            #if the current element is in lowercase, print the current element 
#                        print (written_days) 
#        print(words[2])

fhand = open('For Unit 7 Exercise.txt')
count = 0
for line in fhand:
    words = line.split()
# print('Debug:', words)
    if len(words) == 0 or words[0] != 'From':
        continue
    print(words[2])