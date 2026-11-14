# Function Continue
# We can make empty function and used pass keyword for future used in 

def empty_function():
    pass


# Parameters vs arguments

def full_name(fname,lname): # Variable used while make the functions are known as parameters
    return(fname + ' ' + lname)


print(full_name('Usama','Sohail')) # Values passing while calling the functions are know as argumnets


# Defualt Anguments

def full_name_default(fname,lname="Sohail"): # Making one value as default soo no error will occur while leaving one argument only
    return(fname + ' ' + lname)

print(full_name_default('Usama','Khan'))

# Type Casting
def full_name_def(fname:str,lname:str="Sohail"):
    return(fname + ' ' + lname)

val = full_name_def('usama','sohail')
print(val)




#  *args -> Star Arguments we use it when we don't know how many number of arguments we need 


def my_fuc(*fruit):
    print('The Best Fruit Is ' , fruit[3])

my_fuc('apple','orange','banana' , 'grapes' , 'mango') 


def greets(greetings,*name):
    for i in name:
        print(greetings,i)


greets('Aslam O Alikum' , "Usama" , "Faryal" , "Ayan" , "Jawwad" , "uzair")


# **kwargs

def intro(**myself):
    print("My Name Is " , myself['name'] , 'I:\'am a' , myself['work'] , "My Age Is "  , myself['age'])


intro(name= "Usama Sohail" , work = "Sofware Engineer"  , age = 23)


# Scope Of Variable
def my_funcs():
    x=200
    def printfunc():
        print(x)
    printfunc()


my_funcs()