## We have a list of names, we want to print the list of all names that have  r/R in them. how can we do that?

random_list = ['cable', 'rabbit', 'Ramen', 'cup', 'risk']

# loop over the list
# loop over elements character
# check for r/R
# if found then add it to a seperate list
# print that list

new_list = []

# for i in random_list:
#     for j in i:
#         if j == 'r' or j == 'R':
#             new_list.append(i)

# print(new_list)

### I am writing the above code in more readable format now

# for word in random_list:
#     for char in word:
#         if char == 'r' or char == 'R':
#             new_list.append(word)

# print(new_list)

### Another method to do it

# for word in random_list:
#     if 'r' in word or 'R' in word:
#         new_list.append(word)

# print(new_list)


### We can write the above code in just 3 lines by using list comprehension

names_with_r = [name for name in random_list if 'r' in name.lower()]
print(names_with_r)

### Syntax for list comprehension
### new_list = [expression for iter in sequence if condition]

###  order of if condition and for loop can be changed

### we can also add multiple forloops in this
