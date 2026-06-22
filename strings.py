# name0 = 'Nilanshu sharma is great'
# name1 = ('Ni'
#          'la'
#          'n'
#          'shu')
# name2 = '''abc
# def
# geh'''
#
# print(name0)
# print(name1)
# print(name2)
#
# ### We can use single inverted comma or triple inverted comma and write the sentence in multiple line as i did in the above example. In the name1 i just hit enter and the syntax maintained and i was able to write my sentence "Nilanshu" in it
#
#
# name = 'Nilanshu'
# middle_name = 'Rich'
# last_name = 'sharma'
#
# full_name = name + ' ' + middle_name + ' ' + last_name
# print(full_name)
#
# text = 'My age is: '
# age = 18
#
# # SO currently my age is integer and we cannot add integer with string otherwise it will throw an error so we will convert this age into string
#
# result = text + str(age)
# print(result)

# To get the length of the string
#
# my_name = input('what is your name?')
# print(len(my_name))
# ##// but it count the space also in length
#
# ##To get any particular character from the string input we can do this, here the number represent the index number
#
# print(my_name[0])
#
# ## To get the last character of any string we can do this
#
# last_char_index = len(my_name) - 1
# print(my_name[last_char_index])
#
# ## But in python we have a special way of doing it, when we have to access the characters from the last so in python we have negative indexes.
# '''
# e.g
#  N  I  L  A  N  S  H  U
#  0  2  3  4  5  6  7  8
# -8 -7 -6 -5 -4 -3 -2 -1
#
# from the reverse side the index numbering start from -1 because zero is already taken.
#
# '''
#
# new_last_char_index = -1
#
# print(my_name[new_last_char_index])
# print(my_name[-    2]) # even if there's space, it will run and it won't matter

### we cannot change the string characters of a string via direct assignment like name[0] = 'j'

# name5 = 'Human'
# print('Before', id(name5))
# name5 = 'Human' + 'Being'
# print ('After', id(name5))
#
# print(name5)

### Here it worked but these two are different variables and we can check it via using python id function. and when we print the id number we can see both are different numbers

### Here we tried to reassign the string but instead of reassigning, behind the scene new variable was created. and this shows us the concept of string immutability. so strings are immutable and their values can not be changed after it's creation and if they are changed then a new variable string is created behind the scene

##String slicing
#
# # Here we want range of characters from a string, let's say range from 1st index to 2nd index
#
# name6 = "Tiffin"
# print(name6[1], name6[2])
#
# # In the above example we got the output we wanted but it's not exactly a range, we are just prinitng out 2 characters and certain indexes
#
# # So to get range of characters from a string we need to do this and we will get the range of charcters from the index 1 to index 4. Colon : is used to tell that we want range. but i exclues the end index. so in below example index 4 was not included, only index 1,2,3 got printed
#
# print(name6[1:4])
#
# # when we want to get range of characters we do not need to specify the starting index if it's going to start from 0. like even if we don't mention it python will automatically start it from zero
#
# print(name6[0:4])
# print(name6[:4])
#
#
# # and we can do the same for the ending index
#
# print(name6[0:6])
# print(name6[0:])
#
# # If we mention a larger number than the actual index length at the end then it won't throw error and it will simply print all the available string which is there
#
# print(name6[2:100])
#
# # If I want  to display alternative characters of a string then i can do it
#
# print(name6[::2]) #// This line means It goes from begining of the string to end of string skipping one character every single time
#
# # This allow us to start the range from 1 and then skipping alternative character
# print(name6[1::2])
#
# # If I have to print Tiffi only then I can do this as well, The end index isn't included
#
# print(name6[0:-1])

#String formatting
'''Importatn concept'''

# job = 'Founder'
# location = 'Noida'
#
# formatted_string = 'I am {}, and I am from {}'.format(job, location)
#
# print(formatted_string)
#
# ## The above code works fine but the problem is if we change the order of job and location, the whole sentence will be meaningless. you can think of it like positional arguments. and later we learned about named arguments. so here
#
# new_formatted_string = 'I am {job}, and I am from {location}'.format(location=location,job=job)
#
# print(new_formatted_string)
#
# ## Now even if we change the order the sentence will not get messed up.
#
#
# ## We can also put space in the line in string
#
# new_string = 'Job: {job} Location: {location}'.format(location=location, job=job)
#
# print (new_string)
#
# ### TO put space we will do this
#
#
# new_string = 'Job: {job:10} Location: {location}, India'.format(location=location, job=job)
#
# print (new_string)
#
# ### This 10 represents 10 characters of space
#
# new_string2 = 'Job: {job:10} Location: {location:8}, India'.format(location=location, job=job)
#
# print (new_string2)
#
# ### Now as we can see there is space between noida and india too but let's say we want noida and india together and want space between location and noida then we can use > sign. "<" this is for left hand side and > this is for right hand side
#
# new_string3 = 'Job: {job:10} Location: {location:>8}, India'.format(location=location, job=job)
#
# print (new_string3)
#
# ### This ^ sign centre the text.
#
# new_string4 = 'Job: {job:10} Location: {location:^8}, India'.format(location=location, job=job)
#
# print (new_string4)
#
# ### There's a better way of creating formatted string, which is much simpler and clean
#
# ### When we put "f" in the beginning of the string, we can simply wrap out variable name in the curly brackets and it will automatically take the values of those variables.
#
# better_formatted_string = f"I am {job} and I am from {location}"
#
# print(better_formatted_string)

# pi = 3.14159
#
# print(f"value of pi is {pi:.3f}")

### Here we want to print and display the value of pi upto 3 decimal points only to the user. so we are using :.3f
#
# definition = 'This is a backslash \\'
# print(definition)
#
# ### If we use single backslash python will think this backslash has some special meaning and when you add 2 backslash instead of 1, it knows okay this is just part of the string
#
# definition2 = 'This is a laptop \t this is nice'
# print(definition2)
#
# ### \t adds a tab spcae between the sentence
#
# definition3 = input('What\'s your name?\n')
# print(definition3)
#
# ### Now when we use \n at the last, when the user input anything it will be shown in next line


#
# Name = 'Nilanshu the great'
# print(Name.upper()) # .upper converts  every single character into uppercase
#
# Name2 = 'Nilanshu the great'
# print(Name2.lower()) # .lower converts  every single character into lowercase
#
# Name = 'nilanshu the great'
# print(Name.capitalize()) # .capitalize converts the first character of string into uppercase
#
# Name = 'Nilanshu the great'
# print(Name.title())  # .title capitalize the first word of whole string, like for every single word
#
#
# Name = '            Nilanshu the great         '
# print(Name)
# print(Name.strip())  #.strip removes the spaces from the string, it removes all the space from the left of first character and all the spaces from the right of last character. while it maintain the spaces between the words of sentence in the string
#
#
# Name = 'Nilanshu the great'
# print(Name.replace('a','#')) #.replace replaces the characters in the whole string
#
# Name = 'Nilanshu the great'
# print(Name.count('n')) # .count counts the particular character in the string
#
# Name = 'Nilanshu the great'
# print(' '.join(Name)) # put whatever you want inside the single quote and it will put it in between each character of the string
# print(','.join(Name))


### We can check the equality of string

# device = 'Mobile'
# device_lowercase = device.lower()
#
# print(device == device_lowercase) #//output: false
#
# ### we can check if certain work or gorup of characters are present in the string or not
#
# New_name = 'I am a great coder'
# print('der' in New_name) # this code means if der is presernt in New_name or not
#
# print('e' not in New_name)