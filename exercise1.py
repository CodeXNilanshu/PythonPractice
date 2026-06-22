##write a python program that takes two integers input from the user and print their sum

num1 = input('Enter the first number: ')
num2 = input('Enter the second number: ')

print(num1 + num2)
## we cannot perform this operation, because the num1 and num2 are string not integer, so it will add the strings

'''input always returns the output in string format'''

print(int(num1) + int(num2))

### we do not need to write pirnt() when we use input(), input will automatically print the text we will write inside it

