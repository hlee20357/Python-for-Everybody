#Unit 3 Exercises: Conditional Execution 

#Exercise 1: 

#Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

hours = input('Enter hours: ')
rate = input ('Enter rate: ')
hoursint= float(hours) 
#changes the output of hours (which is a string) to a integer

rateint = float(rate)
#changes the output of rate (which is a string) to a integer

#print (hoursint)
#print (rateint)
if hoursint <= 40:
    Pay = hoursint*rateint
else:
    Pay= ((hoursint-40)*(rateint*1.5)+(40*rateint))
print ("Pay:", Pay)
print (type(Pay))

#Exercise 2: 

#Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. 
# The following shows two executions of the program:

#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input

#Enter Hours: forty
#Error, please enter numeric input

hours = input('Enter hours: ')
try: 
    hoursint= int(hours) #changes the output of hours (which is a string) to a integer
    rate = input ('Enter rate: ')
    try: 
        rateint = float(rate)#changes the output of rate (which is a string) to a integer
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

#Exercise 3: 

#Write a program to prompt for a score between 0.0 and 1.0. 
# If the score is out of range, print an error message. If the score is between 0.0 and 1.0, print a grade using the following table:

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

#Run the program repeatedly as shown above to test the various different values for input.

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
    print ('Error. Please enter a numberic input')
