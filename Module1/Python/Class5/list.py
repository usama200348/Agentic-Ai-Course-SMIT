import os

# List are mutable(changeable elements) and ordered(indexed aligned)

# LIST CONTINUE

fruits = ['apple' , 'mango' , 'banana' , 'peach' , 'kiwi',"kiwi"]
print(fruits)
# print(type(fruits))

# By Default Pop will remove the last element
# print(fruits.pop(2))
fruits.remove('apple')
print(fruits)
os.system('cls')
fruits2 = ['watermelon' , 'guava' , 'kiwi']
# EXTEND
fruits.extend(fruits) # To Merge tHe both list we use extend
print(fruits)
# fruits.clear()
print(fruits)
os.system('cls');
# For Sorting
print(fruits)
fruits.append('apple')
fruits.sort()
print(fruits)
fruits_rev = fruits.sort(reverse=True)
fruits.sort(reverse=True)
print(fruits)
# REVERSE THE EXISTING LIST
fruits.reverse()
print(fruits)
os.system('cls')
# This Is THe SOftcop
fruits_copy = fruits
print(fruits_copy)
fruits_copy.pop()
print(fruits_copy)
print(fruits)
os.system('cls')
# softcopy is a copy of address
fruits_copy = fruits.copy();
fruits_copy.append('kella')
print("Softcopy",fruits)
print("Hardcopy",fruits_copy)

# LENGTH OF THE LIST
os.system('cls')
print(len(fruits_copy))
fruits3 = ['apple' , 'mango' , 'banana' , 'peach' , 'kiwi',"kiwi"]
print(fruits3)