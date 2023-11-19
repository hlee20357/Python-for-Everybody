#Unit 2 Exercises: Variables, Expressions, and Statements 

#Exercise 1: Type the following statements in the Python interpreter to see what they do:
#5
#x = 5
#x + 1

5
x=5
x+1

#Without any print statements, nothing appears on the screen. 
#x is saved as integer 5. 


#Exercise 2

#Write a program that uses input to prompt a user for their name and then welcomes them.

#Enter your name: Chuck
#Hello Chuck

name =input('Enter your name: ');
print ('Hello', name); 
#the comma allows you to print the variable "input" aka the input that you put in from the first command in the same line as "hello"

#Exercise 3: 

#Write a program to prompt the user for hours and rate per hour to compute gross pay.

#Enter Hours: 35
#Enter Rate: 2.75
#Pay: 96.25

#We won’t worry about making sure our pay has exactly two digits after the decimal place for now. 
# If you want, you can play with the built-in Python round function to properly round the resulting pay to two decimal places.

hours = input('Enter hours: ')
rate = input ('Enter rate: ')
hoursint= int(hours) 
#changes the output of hours (which is a string) to a integer
rateint = float(rate)
#changes the output of rate (which is a string) to a integer
Pay = hoursint*rateint
print ("Pay:", Pay)
print (type(Pay))

#Exercise 4: 

#Assume that we execute the following assignment statements:

width = 17
height = 12.0

#For each of the following expressions, write the value of the expression and the type (of the value of the expression).
#1. width//2
#2. width/2.0
#3. height/3
#4. 1 + 2 * 5

#Use the Python interpreter to check your answers.

print (width//2) 
#Answer is 8, class of integer
print (width/2.0) 
#Answer is 8.5, class float
print (height/3) 
#Answer is 4.0, class float 
print (1+2*5) 
#Answer is 11, class integer

#Exercise 5: 

# Write a program which prompts the user for a Celsius temperature, 
# convert the temperature to Fahrenheit, 
# and print out the converted temperature.

temperature = input ('What Celsius temperature would you like to convert to Fahrenheit? Enter numbers only: ')
temperature = float(temperature)
Fahrenheit = (temperature*1.8)+32
Fahrenheit = str(Fahrenheit)
print ('The conversion to Fahrenheit is ' + Fahrenheit + '.')
