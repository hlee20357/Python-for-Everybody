# checking if string contains list element
# using list comprehension
 
# initializing string
test = ["There are 2 APPLES for 4 persons", "There are 3 cucumbers", "there are 5 oranges"]
 
# initializing test list
test_list = ['apples', 'oranges']
 
 
# printing original list
#print("The original list : " + str(test_list))
 
# using list comprehension
# checking if string contains list element
res = any(ele in test for ele in test_list)
 
# print result
#print("Does string contain any list element : " + str(res))

#print (res)
#for index in test: 
#    print (index)
#    if any(ele in test for ele in test_list):
#        print ("I was here")
#        #seems you can't use any() to compare between lists. 
#        for fruit in (test_list): 
#            if fruit in test_string: 
#                print (fruit)

for index in test: 
    if any(test_list) in test:
        print ("hi")
        for fruit in (test_list): 
            if fruit in test_string: 
                print (fruit)
