from time import sleep
from random import choice
my_list = ["apple", "banana", "grape", "1", "2", "3"]
# my_list.pop(), removes last item from list
#make it a variable
# del my_list[position]

print(my_list[0])
for iiitwm in my_list:
    print(iiitwm)
my_list.append("pumpkin")
print(my_list[-1])
my_list.insert(1, "watermelon")
my_fruit = choice(my_list)
# while True:
# print(my_fruit)
people = ["Jude", "Ian", "William", "Zakk", "Antoine", "Ethan"]
while True:
    person = choice(people)
    sleep(1)
    print(person)