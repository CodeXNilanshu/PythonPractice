### if condition:
###   statement
###   statement
###   statement

### i have to leave space on the left hand side for the statement. All the statements after colon (:) which are indented using space are body of the if statement

### Indentation are basically the white spaces before the statement. It carries special meaning in python and it is a way of telling python intrepretor that that these particular statement belong to particular code of block

## we can create the indentation via either  with space or with tab. e.g. if you created a indetation using 2 spaces then throughout the code block you have to give two spaces to tell the inrepretor that this is statement and belong to this code of block

# age =18
#
# if age > 18:
#     print('you can work')
# elif age == 18 :
#     print('Consult your parents first')
# else:
#     print('you cannot work')

### In python we use "elif" instead of "else if" and it's compulsory to use cuz "else if" doesn't exist in python

###Empty string return false, but string with only space still returns true.

# name = input('Enter your name')
# name = name.strip()
#
# if name:
#     print(name)


### This is nested  if  else condition
#
# number = int(input('Enter a number: '))
#
# if number >=0:
#     print('Number is positive')
#     if number % 2 ==0:
#         print('Number is even')
#     else :
#         print('Number is odd')
# else:
#     print('Number is negative')
#
