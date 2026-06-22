#username = input ('what is your name?')
#print ('Hello', username)
#print('How\'s it going', username)

'''Definition of Variable : It is a named area of computer's memory that can be used to hold data. variable is just refrencing the stored data. so the "username" is just referencing  the area of the computer memory which is holding my data.'''


## print(name)  // It will show error the variable name should be declared before accessing it
#name = 'I am genius'
#print(name)


'''variable names are case sensitive, all these are differnt variables'''

# city = 'kota'
# City = 'delhi'
# CIty = 'Banglore'

# print(City)
##//output : delhi

'''By convention we should use underscore if the name has seperate words, even if we not do it, there won't be any error but we should follow the convention'''

# my_name = 'Nilanshu Sharma'
# print(my_name)

'''we can reassign the variable'''

# my_name = 'Nishu Sharma'
# print(my_name)

# user_type = 'employee'
# user_salary = '3 cr'

# print(user_type, user_salary)

'''we can create multiple variable like this'''

# name, surname = 'Preeti', 'Singh'
# print(name, surname)

'''Let's say the name and surname are same, so we can do this'''

# name = surname = ('Preeti')
# print(name, surname)

'''Let's swap the names and surnames'''
###code line39,40 uncomment for this
### temp = temporary variable

# temp = name
# name = surname
# surname = temp
#
# print(name, surname)

'''The above method was too lengthy so what we can do instead is'''

# name, surname = surname, name
# print(name, surname)

'''we can also delete the variable from the memory by using "del" keyword'''

# del surname
# print(name)

#print(name, surname) # here we get warnning for surname "Name 'surname' can be undefined" and if we run it we get see error in the console "NameError: name 'surname' is not defined"

