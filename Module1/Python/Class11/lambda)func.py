# Lambda function
# Many Arguments but one expression
# Lambda apko function bana ka daa ga
 

import os

x = lambda a:a+10
print(x(20))

# Multiple Arguments
y = lambda a,b: a+b
print(y(22,22))


z = lambda a,b : "Hello World "+ a + ' and '+ b + ' How Are You'
print(z('Usama','Aliyan'))


# Function use case

def myfunc(num):
    return lambda a:a+num


my_adder = myfunc(10)
print(type(my_adder))
print(my_adder(2))


# Recusrion
# recursion using function as an loop 

os.system('cls')

def count_down(n):
    if n <=0:
        print("Done")
    else:
        print(n)
        count_down(n-1)

count_down(5)



# Factorial Function


def factorial(n):
    # Base Case
    if n==0 or n==1:
        return 1
    # Recursive Case
    else:
        return n * factorial(n-1)
# 5*4*3*2*1*1
print(factorial(5))