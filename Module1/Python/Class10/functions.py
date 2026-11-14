import math
# Functions
# They Provide code resuability
# They Provide easy maintance
# They Provide Clean Code

#Function Defination
#Actual Code Snippet of Function

# Function Is Identifed by "def"
'''
Syntax
python keyword 'def' is used to create function
def function name 
'''


# Function Initilized
def this_function():
    print("This IS A Function");


# Function Call
# this_function()


# Function To convert fahrenite to centigrade
num = 100
def temp_f_to_c():
    calc = (num-32)*5/9
    print(math.floor(calc*100)/100)

temp_f_to_c()

# Function With Parameter

def f_2_c(num):
    calc = (num-32)*5/9
    converted = math.floor(calc*100)/100
    print(converted)

f_2_c(55)

# Calculating Area

def area(l,b):
    print(l*b)

area(5,2)

# Ordering In Parameters in imp

def salary_cal(amount,tax,allowance):
    gross_sal = amount + allowance
    net_sal = gross_sal - gross_sal*tax/100
    converted = math.floor(net_sal*100)/100
    print(converted)

# Wrong Result Expected
salary_cal(200000,25,50000)
# Correct way
salary_cal(amount=200000,allowance=50000,tax=25)

# 

def is_vowel(letter):
    if letter in ['a','e','i','o','u']:
        return "Letter Is Vowel"
    # Return used to return the output value
    else:
        return "Letter Is Not Vowel"
    
value = is_vowel('z')
print(value)

