grocery = []
while True:
    item = input("What item would you like to add to your list? > ")
    grocery.append(item)
    if item == "":
        grocery.remove(item)
        break
print(grocery)