import os
# LIST

# LIST Are used to store multiple items in a single variable

fruits = 'apple , mango , banana , peach , kiwi , pear , pineapple , grapes , orange';

print(type(fruits))
os.system('cls');
var = fruits.split(',')
print(var)
var = fruits.replace(' ' , '').split(',')
print(type(var))
print(var[2].strip())

# List INDEXES  And Slicing is same as string
print(var[0:2])
print(var[:2])
print(var[-2])
print(var[4:])

# APPEND (Adding Elements IN A List);
var.append("Strawberry")
print(var)
# For Appropiate Adding Element In a list we use insert
var.insert(0,'avacado')
print(var)
# Changing an element
os.system('cls')
var [7] = "Usama"
print(var)
# For Removal 
var.pop();
print(var)

# By default pop will remove the last element and we can also give the specific index to remove the element
# var.pop(2)
var.remove('apple')
print(var)