# For Loop Where we don't know the condition


# RANGE
# RANGE (start,end, step/interval)
# for var_name range(start,end,step/interval)


import os
for num in range(1,10,1):
    print(num)


    # Reverse (counting)
for num in range(10,1,-1):
    print(num)

os.system('cls')

# List In Loop 
lst = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

# Option1 :
for i in range(len(lst)):
    print(lst[i] , "at Index " , i)

os.system('cls')

for i in lst:
    print(i)


    # Loop On Strings
os.system('cls')
string =  "Usama Sohail"

for i in string:
    if i==' ':
        continue
    elif i == 'o':
        print('Sohail')
        continue
    print(i)