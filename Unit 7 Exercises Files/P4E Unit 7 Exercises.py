#Exercise 1
#Write a program to read through a file and print the contents of the file (line by line) all in upper case. 
#File from www.py4e.com/code3/mbox-short.txt

#python shout.py
#Enter a file name: mbox-short.txt
#FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
#RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
#RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
#BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
#SAT, 05 JAN 2008 09:14:16 -0500

#Example above is what your output should like look 
import os 
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
fhand2 = open('mbox.txt')

print ('')
#inp = fhand.read()
#print (fhand)
#print (len(inp))
#print (inp[:20])
#Code above to confirm that I was able to open the file 

#for line in fhand: 
#    line = line.upper()
#    print (line)

#Can't use the code below to make all the lines uppercase. 
#This is because inp makes all the lines and new line characters be combined into one big string in variable inp 
#Therefore, the for loop is going through each character and making it uppercase. 
#for line in inp: 
#    line = line.upper()
#    print (line)

#Exercise 2
#Write a program to prompt for a file name, and then read through the file and look for lines of the form:

#X-DSPAM-Confidence: 0.8475

#When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract the floating-point number on the line.
#Count these lines and then compute the total of the spam confidence values from these lines.
# When you reach the end of the file, print out the average spam confidence.

#Enter the file name: mbox.txt
#Average spam confidence: 0.894128046745
#Enter the file name: mbox-short.txt
#Average spam confidence: 0.750718518519

#Test your file on the mbox.txt and mbox-short.txt files.

def calc_spam_confidence(fhand):
    total_sum = 0
    count = 0 
    #initalize the counting variables before you go into the for loop so that you don't reset the counting variables as you go through the for loop 
    for line in fhand: 
        if 'X-DSPAM-Confidence' in line: 
            y = len(line)
            extract_spam_value = float(line[20:y])
            #Need to make the extract_spam_value a float because line[20:y] is originally a string 
            total_sum = total_sum + extract_spam_value
            count = count + 1
    average = total_sum/count 
    return (average)

print ('File name: mbox-short.txt')
print('Average spam confidence: ', calc_spam_confidence(fhand))
print('')
print ('File name: mbox.txt')
print ('Average spam confidence: ', calc_spam_confidence(fhand2))

#The print statements print out the average spam confidence for mbox-short.txt and mbox.txt
#The values printed are what the exercise stated it should be for the respective files. 

#Exercise 3

#Sometimes when programmers get bored or want to have a bit of fun, they add a harmless Easter Egg to their program. 
# Modify the program that prompts the user for the file name so that it prints a funny message when the user types in the exact file name “na na boo boo”. 
# The program should behave normally for all other files which exist and don’t exist. 

# Here is a sample execution of the program: 
# python egg.py
#Enter the file name: mbox.txt
#There were 1797 subject lines in mbox.txt

#python egg.py
#Enter the file name: missing.tyxt
#File cannot be opened: missing.tyxt

#python egg.py
#Enter the file name: na na boo boo
#NA NA BOO BOO TO YOU - You have been punk'd!

#We are not encouraging you to put Easter Eggs in your programs; this is just an exercise.

def determine_number_of_lines(fhand, fname):
    count = 0 
    for line in fhand: 
        if line.startswith('Subject: '): 
            count = count + 1
    return ('There were ', count, ' subject lines in', fname)

fname = input('Enter a file name: ')
if fname == 'na na boo boo': 
    print ('Na Na BOO BOO TO YOU - You have been punked!') 
    exit()
try: 
    fhand = open(fname)
except: 
    print ('File cannot be opened: ', fname)
    exit()
print (determine_number_of_lines(fhand, fname))

#When testing the code, it works in all three occasions for mbox.txt, missing.tyxt, and na na boo boo