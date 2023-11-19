#Unit 6 Strings Exercises

#Exercise 1

#Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.

fruit = 'apple'
index = len(fruit)-1
while index < len(fruit) and index>=0:
    reverse_order_letter = fruit[index]
    print(reverse_order_letter)
    index = index - 1

#Exercise 2

#Given that fruit is a string, what does fruit[:] mean?

fruit = 'watermelon'
print (fruit[3:] + '.', 'This character splicing prints out index 3 (being inclusive) and beyond')
print (fruit[:3] + '.', 'This character splicing prints out indicies 0 to 2. This is because the y in [x:y] is excluded in the character splicing')
print (fruit[3:3] + '.', 'This is an empty string.')
print (fruit[:] + '.', 'This just prints the whole variable because no argument is taken essentially.')

#Exercise 3

#Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments.

#Code in question

#word = 'banana'
#count = 0
#for letter in word:
    #if letter == 'a':
    #count = count + 1
#print(count)

input_word = 'python for everybody'
input_letter = 'e'

def count_the_letters(word,letter):
    count=0 
    for cycling_one_by_one in word: 
        if cycling_one_by_one == letter:
            count = count + 1 
    print('The number of', letter, 'in', word, 'is', str(count) + '.')
    return count 

count_the_letters(input_word, input_letter)

#Exercise 4

#There is a string method called count that is similar to the function in the previous exercise. Read the documentation of this method at:
#https://docs.python.org/library/stdtypes.html#string-methods

#Write an invocation that counts the number of times the letter a occurs in “banana”.

word = 'banana'

print ('The number of times the letter a is present in banana:', word.count('a'))
#print out the number of 'a' in 'banana'

#Exercise 5

#Take the following Python code that stores a string:

#str = 'X-DSPAM-Confidence:0.8475'

#Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extracted string into a floating point number.

Str = ‘X-DSPAM-Confidence:0.8475’ 
position_start = Str.find('0.8475')
print ('Index position start of 0.8475 in string:',Str.find('0.8475'))
Position_end = (Str.find('5'))
print ('Index position end of 0.8475 in string:', Str.find('5'))
extraction = Str[19:25]
print ('String extraction:', extraction)
print ('Type of the string extraction:', type(extraction))
floating_number = float(extraction)
print ('With the float function, the floating number is now:',floating_number)
print ('Confirming whether number printed above is a floating number:', type(floating_number))