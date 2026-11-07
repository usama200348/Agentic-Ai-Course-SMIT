import os
# While Loop
num = 1 
while num < 10 :
    print(num)
    num = num + 1
print('END')

os.system('cls')
# Breaking In Loop 
number = 1
while number<10:
    # Loop Body
    print(number)
    if number==5:
        print("Break")
        break
    number = number+1
print("End Loop")


# Continue In Loop
os.system('cls')
numbers = 1
while numbers<10:
    # Loop Body
    numbers = numbers+1
    print(numbers)
    if numbers==5:
        continue
print('End Loop :\'( ')


