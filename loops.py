
'''WHILE LOOPS'''
### WHILE LOOPS

# while condition:
#     statement
#     statement
#     statement

# i = 0
#
# while i <=5 :
#     print(i)
#     i += 1
# else: #This else condition only executes once when the while loop is completed
#     print(i)


### Here we are printing a right angle triangle with "*"
# j = 1
# while j<=6:
#     print("*" * j)
#     j += 1
# else:
#     print('Here\'s your right angle triangle')

# name = 'Nilanshu'
# length = len(name)
# k = 0
# while k <= length -1:
#     print(name[k])
#     k += 1
# else:
#     print('done')

### Loop over list or iterating over list

# names = ['Nil', 'Prajakta', 'Natasha', 'Cool boy']
# names_length = len(names)
# n = 0

# while n < names_length:
#     print(names[n])
#     n = n+1
# else:
#     print('Done')

### To find a particular name from the list we can do this but to run the below code we have to comment the above while loop

### while n < names_length:
###   if names[n] == 'Prajakta':
###        print(names[n])
###     n = n+1
### else:
###     print('Done')

### We can use break keyword to break out of loop and this works even when the condition is true for while loop

# while n < names_length:
#     if names[n] == 'Prajakta':
#         print(names[n])
#         break # it breaks the loop, this is inside the if condition so it will only break if the 'Prajakta" is found
#     n = n+1
# else:
#     print('Done')


#
# while n < names_length:
#     if names[n] == 'Prajakta':
#         print(names[n])
#         continue ### If we use continue instead of break keyword then the loop keep continuing and become the infinite loop, because it will never allow the interpretor to reach the line where n is increamenting by so it will always be zero and the if it is always there then it keep looping over again and again cuz the contidition is always true
#     n = n+1
# else:
#     print('Done')



'''FOR LOOPS'''
### FOR LOOPS

### Range Funtion
### range(start, stop, step_size)



# print( range(5) )
# print(range(1,5))
# print(range(1,5,2)) #1, 3
### starting number is not mentioned so it will be considered zero, range will go from zero to five but 5 will be excluded. step_size is 1 by default, if it is not change

### we can also pass negative values as step size

# print(range(5,1,-1)) #5,4,3,2

### Syntax  of for loop
'''Syntax of for loop'''

### for iter in sequence:
###    statement
###    statement
###    statement

### Here "for" keyword will tell python we want to execute "for" loop and "in" is a membership operator.

### A "sequence" can be any sequence like a list, string, range of numbers, it can be any sequence.

### A "iter" is a variable that takes the value of each item in the

# for i in range(1,5):
#     print(i)
#
# ### unlike while loop we don't have to increment the value of i or anything
#
# print('abcd')
#
# for i in range(1,5,2):
#     print(i)


# names = ['Nishu', 'CodingGod', 'Zoro', 'Nami']

# for name in names:
#     print(name)

###  The above code loop through the list while the the below code loop through the name characters
name = 'Rivaan'

# for char in name: # This one prints the characters
#     print (char)

# for i in range(len(name)): #This one prints the characters as well as index of those characters
#     print(i, name[i])

### We can use enumerate function instead of above code to do the same task
### enumerate() -> count/index, char

# for i, char in enumerate(name):
#     print(i, char)


"""Difference between For and While loop"""
### for loop are used when we need to loop over are known before hand
### while loop are used when no. of elements not known before hand

### for loop : No condition involved, used when we need to go over a sequence
### while loop : Condition involved


