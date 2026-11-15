# DECORATORS
# advancemnet in function (For Adding additional functionalties)


def change_case(func): #Decorator Function
    def my_lower():
        return func().lower()
    return my_lower()
# Calling Decorator Function
@change_case

# Basic Function
def myfunction(): 
    return 'Hello World'
# Calling Basic Function
print(myfunction)


@change_case
def herfunction():
    return 'SAYALANI TECH LIMITED'

print(herfunction)


@change_case
def hisfunction():
    return 'Class 11'

print(hisfunction)


# Decorator And Arguments

def greetings(func):
    def inner(x):
        return 'Hello' + str(x)
    return inner


@greetings
def theirfunc(name):
    return name

print(theirfunc(' Uzair'))

