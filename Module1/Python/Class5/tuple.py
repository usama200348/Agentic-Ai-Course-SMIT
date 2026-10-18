# TUPLES
# Tuples are ORDERED(indexed) but imutable(unchangable)
import os
mytuple = (12 , 543, 6 ,22 , 58 , 'abc')
print(type(mytuple))
print(mytuple)

print(mytuple[3])


# Tuple are imutable
os.system('cls')
# mytuple[0] = "Usama"
print(mytuple[0])
tuple2 = (1,2,2,3,4,5,6)
mytuple = list(mytuple)
print(type(mytuple))
mytuple.append('abx')
print(mytuple)