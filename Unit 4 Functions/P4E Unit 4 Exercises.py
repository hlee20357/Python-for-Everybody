#Unit 4 Exercises: Functions

#Exercise 1: 

#Run the program on your system and see what numbers you get. 
#Run the program more than once and see what numbers you get. 

#Program 
import random

for i in range(10):
    x = random.random()
    print(x)

#Prints out random float numbers between 0 and 1 10 times. 

#Exercise 2: 
# Move the last line of this program to the top, so the function call appears before the definitions. Run the program and see what error message you get. 

#Original Program 

#def print_lyrics():
#print("I'm a lumberjack, and I'm okay.")
#print('I sleep all night and I work all day.')

#def repeat_lyrics():
#print_lyrics()
#print_lyrics()
#repeat_lyrics()

#Revised program

#repeat_lyrics()
#def print_lyrics():
#print("I'm a lumberjack, and I'm okay.")
#print('I sleep all night and I work all day.')

#def repeat_lyrics():
#print_lyrics()
#print_lyrics()

#Outcome: Leads to an NameError message stating that "name 'repeat_lyrics' is not defined"
#This occurs because you called the function before the definitions. 

#Exercise 3: 

#Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat-Lyrics. 
# What happens when you run the program? 

#Original Program 

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print('I sleep all night and I work all day.')

def repeat_lyrics():
    print_lyrics()
    print_lyrics()

repeat_lyrics()

#The outcome is that the program still runs. 
# This is because all of the definitions were defined before the function was called. 
#The contents of print_lyrics is printed twice because repeat_lyrics has 2x of print_lyrics. 
#That's why you see 

#I'm a lumberjack, and I'm okay. 
#I sleep all night, and I work all day. 
#I'm a lumberjack, and I'm okay. 
#I sleep all night, and I work all day. 

#Exercise 4: 

#What is the purpose of the “def” keyword in Python?

#a) It is slang that means “the following code is really cool”
#b) It indicates the start of a function
#c) It indicates that the following indented section of code is to be stored for later
#d) b and c are both true
#e) None of the above

#Answer: D. 
# This is because def is just the keyword for a function definition. 
# A function definition is defined as “a statement that creates a new function, specifying its name, parameters, and the statements that it executes.” 
# Once you call the function, it will recall all the stored statements associated with the function. 

#Exercise 5: 

#What will the following Python program print out? 

def fred():
    print("Zap")
def jane():
    print("ABC")

jane()
fred()
jane()

#a) Zap ABC jane fred jane
#b) Zap ABC Zap
#c) ABC Zap jane
#d) ABC Zap ABC
#e) Zap Zap Zap

#Answer: D. 
#ABC
#Zap
#ABC

#Exercise 6: 

#Rewrite your pay computation with time-and-a-half for over- time and create a function called computepay which takes two parameters (hours and rate).

#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

def computepay():
    hours = input('Enter hours: ')
    try: 
        hoursint= int(hours) 
        #changes the output of hours (which is a string) to a integer
        rate = input ('Enter rate: ')
        try: 
            rateint = float(rate)
            #changes the output of rate (which is a string) to a integer
            print (hoursint)
            print (rateint)
            if hoursint <= 40:
                Pay = hoursint*rateint
            else:
                Pay= ((hoursint-40)*(rateint*1.5)+(40*rateint))
            print ("Pay:", Pay)
            print (type(Pay))
        except: 
            print ('Error. Please enter a numeric input.')
    except: 
        print ('Error. Please enter a numeric input')

computepay()

#Exercise 7: 

#Rewrite the grade program from the previous chapter using a function called computegrade that takes a score as its parameter and returns a grade as a string.

#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F

#Enter score: 0.95
#A

#Enter score: perfect
#Bad score

#Enter score: 10.0
#Bad score

#Enter score: 0.75
#C

#Enter score: 0.5
#F

#Run the program repeatedly to test the various different values for input.

def computegrade(): 
    score = input('Enter score: ')
    try: 
        gradefloat = float(score) #changes the output of hscore (which is a string) to a float
        if gradefloat <0 or gradefloat >=1:
            print ('Bad score')
        elif gradefloat >=0.9 and gradefloat <=1.0: 
            print ('Grade = A')
        elif gradefloat >=0.8 and gradefloat <0.9: 
            print ('Grade = B')
        elif gradefloat >=0.7 and gradefloat <0.8: 
            print ('Grade = C')
        elif gradefloat >=0.6 and gradefloat <0.7: 
            print ('Grade = D')
        elif gradefloat>=0 and gradefloat <0.6: 
            print ('Grade = F')
    except: 
        print ('Error. Please enter a numeric input')
        
computegrade()


