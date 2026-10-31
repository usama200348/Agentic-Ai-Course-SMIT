# SETS
# SETS ARE IMMUTABLE AND UNORDERED


this_set={'apple','mango','orange'}
print(type(this_set))

dup_list = [1,2,3,1,5,6,7]
print(dup_list)
# Removing duplicates

mylist = list(set(dup_list))
print(mylist)

copy = mylist.copy()
print(copy)