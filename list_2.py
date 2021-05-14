# Create an empty list
from random import randint
list = []
for item in range(27):
    list.append(randint(0, 100))
    print(list)
# Sorting list
list.sort()
print(list)
# Reversing the sort
# list.reverse()
print(list)
# Length of list
print("You have", len(list), "items in this list")
# Getting the biggest number
print("Max number is,", max(list))
print("Min number is,", min(list))
# adding all numbers in list
print(sum(list))
# Slicing lists
print(list[:5])