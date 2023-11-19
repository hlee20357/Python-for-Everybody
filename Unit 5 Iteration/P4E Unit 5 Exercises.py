#Unit 5 Iteration Exercises 

#Exercise 1 

#Write a program which repeatedly reads numbers until the user enters “done”. 
#Once “done” is entered, print out the total, count, and average of the numbers. 
#If the user enters anything other than a number, detect their mistake using try and except and print an error message and skip to the next number.


#Enter a number: 4
#Enter a number: 5
#Enter a number: bad data
#Invalid input
#Enter a number: 7
#Enter a number: done
16 3 5.333333333333333

count=0
total=0
while True:
    inp=input('Enter a number: ')
    if inp==('done'):
        break 
    try: 
        testnumber=float(inp)
        print(testnumber,'works!')
        count = count+1
        #print(count)
        total= total+testnumber #program works from right of the equal sign then to the left if you are changing the variable. Basically in this case, it's saying "new" total = old total plus the input number. 
        #print(total)
    except: 
        print('Error. Moving on to the next number.')
print('Done!')
print ('Count: ', count)
print ('Total: ', total)
average = total/count 
print ('Average: ', average)

#Exercise 2: 

#Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

count=0
total=0
while True:
    inp=input('Enter a number: ')
    if inp==('done'):
        break 
        #breaks the while loop so you can get out of it 
    try: 
        testnumber=float(inp)
        print(testnumber,'works!')
        count = count+1
        print('Count in this loop is ', count)
        total= total+testnumber 
        #program works from right of the equal sign then to the left if you are changing the variable. Basically in this case, it's saying "new" total = old total plus the input number. 
        #print('Total in this loop is ', total)
        if count==1: 
        #establishes smallest and largest with the first user input 
            smallest = testnumber
            largest=testnumber
        elif count>1: 
        #now, after every single loop after the initial loop, it'll go through the inputs to see whether the current input was the largest or smallest of a previous input. 
            if testnumber<smallest: 
                smallest = testnumber
            if testnumber>largest: 
                largest = testnumber 
        #print('Largest number from all the loops is ', largest)
        #print('Smallest number from all the loops is ',smallest)
    except: 
        print('Error. Moving on to the next number.')
print('Done!')
print ('Count: ', count)
print ('Total: ', total)
average = total/count 
print ('Average: ', average)
print('Overall largest number from inputs: ', largest)
print('Overall smallest number from inputs: ', smallest)