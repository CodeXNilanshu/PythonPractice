print(1)
print(type(5))
print(type('10'))

# int
"""Integer can be positive and negative. Integer can be of size, It doesn't get restricted like java where we have certain limits for the size of Integer number"""

age = 18
print(age)

money = -20
print(money)

# float
"""These are the numbers having decimal points, and these numbers can be positive and negative as well"""

some_float = 18.2
print(some_float)
print(type(some_float))

'''Float can be representated using the scientific numbers as well like e '''

number = -69.27E100  # here e can be both small or capital, E means a number to the power of 10, the numer we wrote means -69.27*10^100 ## * means multiplications
print(number)
print(type(number))

# complex numbers
# a + bj // here a is the real part and bj is imaginary part e.g. 4 + 5j

num = 4 + 5j
print(num, type(num))

# if we put a = 0 and check if the 0 + 5j will be a complex number or something else

num2 = 3j
print(num2, type(num2))

# we cannot write b as zero like 4 + j, because interpreter cannot identify it the type

# num3 = 4 + j // it throws a compile time error
# But  if we write 1j then it will correctly identify it that its a complex number.

num4 = 4 + 1j
print(num4, type(num4))
num4 = 8
print(num4, type(num4))
num4 = 'Hello'
print(num4, type(num4))

### Here the data type of num4 changed to integer from complex number when we assigned an int to it and then we changed the data type to string

'''In python a variable doesn't have to be of 1 type throughout the program. This is an important property because in language like java and c++ you cannot change the datatype of a variable once it is assigned however variable of one datatype can be changed to another in python

 This is called dynamically typed language
 '''

# we can also do this to change the datatype

float_value = 2.8  # here when converting to int the bare minimum value is taken so integer form will be 2
float_value = int(float_value)
print(float_value, type(float_value))

# To convert int to string we use the keyword "str"

my_age = 24
my_age = str(my_age)
print(my_age, type(my_age))
