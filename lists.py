# names =['Nilanshu', 'Kunal', 'Aditya', 'Prem']
# nums =[1,2,3,4,5]
# some_other = ['Rivaan', 1,2.2, True, 4 + 5j]

### List can contain any data type and we can create a list which can contain lot's of different data type
#
# print(names[0])
# print(names[-1])
# print(names[1:])
# print(names[1:2])
#
# ### '''unpacking a list'''
# name1, name2, name3, name4 = names
# print(name2)
# print(name1, name2, name3, name4) # print allow us to put multipl e inputs

### If we have to just get one input from the list and assign a variable to it we can do it with help of "*"

# name1, *name2 = names
# print(name1, name2)
#
# ### Here the first item in the list got assigned to variable name1 and and right hand side part was saved to name2 as list
#
# name1, *name2, name3 = names
# print(name1, name2, name3)

### Here values from list got saved in name1 and name3 variable and the between values got saved in name2 in list format

### functions of list and strings are similar so you can try all the other cool stuff as well.

### we can get length of list like this
#
# print(len(names)) #//4
# print(len(names[0])) #//8 ... It access the first element of list and then count the characters length of Nilanshu
#
# ### We can create list inside of list like this
#
# list_in_list = [[],[],[]]
#
# ### order of elements matters in list
#
# ### In string we cannot replace but in list we can replace elements, list can contain duplicate values as well
#
# ### To change values in a list
# print(id(names))
# names[-1 ] = 'Sushant'
# print(names)
# print(id(names))
#
# ### In string a new variable with other id was being created when we were reassigning it but in list it doesn't happen, Id remains the same
#
# ### Strings are immutable, while lists are mutable, means they can be changed after they are created
#
# names[:3] = ['Damn', 'Boi'] #we added only two elements but the range was of 3 elements 0,1,2 (3 is excluded) so it deleted the third element automatically.
# print(names)
#
# ### In the above code we replaces the starting elements of the names list with new elements
#
# ### also if the range mentioned is less and the elements we want to add are more than the elements will get added and it won't show any error and neither it will delete anything
#
# names[:2] = ['Damn', 'Boi', 'Sus']
# print(names)
#
# names[0] = [1,2]
# print(names)
#
# ### We can add two lists as well
#
# dummy = [1,1,1,1,1]
#
# print(names + dummy)
#
# ### If we use multiplication then the elements will get multiplied inside the single list. It basically creates a new list and repeat the list the number of time your mentioned
#
# print(names * 3)
#
# ### TO ADD A NEW ELEMENT
#
# ### We cannot add a new element to the list by assining a new index with new value. it will throw error
#
# ### To add value to the list
#
# names.append('batman')
# print(names)
#
# ### No new list was created in the above code, it's the same variable as before, In list, it updates the original list.
#
# ### TO INSERT AN ELEMENT AT PARTICULAR INDEX IN LIST
#
# names.insert(0, 'luffy')
# print(names)
#
# ### TO REMOVE THE LAST ELEMENT OF LIST
#
# name = names.pop()
# print(names)
# print(name)
#
# ### we can check which element was removed by assigning the method to a variable
#
# names.remove('Boi')
# print(names)
#
# ### If there are duplicate elements in your list then it will only remove the first element it encounters, and won't delete every single one of them
#
#
# ### We can get the index of any element via this

# print(names.index('Nilanshu'))
#
# ### we can sort the list with this
# names.sort()
# print(names)
#
# ### we can put certain condition of sorting inside this sort()
#
# print('Nilanshu' in names)
#
# ### JOIN METHOD
#
# print(', '.join(names) )
#
# ### Remove all the elements from the list
#
# names.clear()
#
# print(names)


'''Copying a list'''

### COPYING A LIST

### Copying a list does not create a new list but it actually refers to the copied list and if we make any changes to the new list then the original list will also be influenced
#
# new = ['cat', 'dog', 'dinosaur']
# other = [1,2,3,4]
#
# new = other
#
# print(new)
# print(other)
#
# new.append(5) #[1,2,3,4,5]
# other.append(6) #[1,2,3,4,6]
#
# print(new)
# print(other)

### In above example both the variables are pointing to the same list and hence if we make changes with any of the variable then the orgional list will be changed and in actual there's no creation of new list, it's just the new variable is also pointing toward the location of memory where the list was placed.


other1 = [1,2,3,4]
new1 = ['cat', 'dog', 'dinosaur', other1]

### In the above code if we just put variable name in the new1 list then if there's any changes in the other1 list, it will reflect in the new1 list as well. and to avoid such this and truely make a copy of the list we can do something like this "other1[:]". "[:]" basically go from starting of the list to the end and copy it and create a new list.
#
# new2 = ['cat', 'dog', 'dinosaur', other1[:]]
#
# other1.append(5)
# print(new1)
# print(new2)

### Now as we can see in output the new2 list doesn't change even if there's change in the other1











