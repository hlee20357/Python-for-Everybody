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

    #checks if the list words has greater than 0 elements 
    #checks if the first element in the list words is "From"
    #checks if any words in the lowercase string are one of the elements in the list days. Outputs a true or false statement. 
    #If true for all, then you move forward. 
#        for written_days in days: 
        #for loop to go through each element in days list. written_days is the iterating variable. 
 #           if written_days in words: 
            #if the current element is in the list, print the current element 
  #              print (written_days) 
   #             continue
                #once the print statement is executed, you can move on to the next line because there is only one written_day in the specific line. 
                