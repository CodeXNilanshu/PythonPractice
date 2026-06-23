### BODMAS - Brackets, Orders (powers and square roots), Division and Multiplication, and Addition and Subtraction.

## Unary Operators
## -5

## Certain operators take precedence over other operators and based on the type of operator and their precedence calculations are made, You can check the precedence table of python operators online

 ## Link for the precedence table : https://www.programiz.com/python-programming/precedence-associativity

## Binary Operators

## Excercise 3 :

# You are developing a simple authentication system for a secure facility.
# The system needs to verify the identity of a person based on their credentials.
# The person is granted access only if they meet either of the following
# conditions:

# 1. They have a valid access code i.e. a 4-digit numerical code.
# 2. They are a member of the access list, which contains the following
#    members: 69, 420, 69420.
# Write a Python program that prompts the user to enter their access code and
# checks whether they are allowed access based on the conditions mentioned above.
# Display a message indicating whether access is granted or denied.


user_input = input('Enter the credentials: ')

deny_message = 'Access Denied'
grant_message = 'Access Granted'

int_user_input = int(user_input)

user_input_value = int_user_input == 69 or int_user_input ==  420 or int_user_input ==  69420 #//true/false

user_input_length = (len(user_input))

checking = int(user_input_length) == 4 or user_input_value

not_checking =  not checking

print(grant_message * checking + deny_message * not_checking )


### It works but I have to write the program without if else condition so I am using above method
# if checking:
#     print(grant_message)
# else:
#     print(deny_message)





