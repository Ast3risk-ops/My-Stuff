import random
from time import sleep
from sys import exit
stuff = ["Jude", "Ian", "penut", "butt jim", "butt jimm", "butttttt, jim", "jim butt", "a", "Ethan", "10"]
while len(stuff) != 0:
    thing1 = random.choice(stuff)
    stuff.remove(thing1)
    thing2 = random.choice(stuff)
    stuff.remove(thing2)
    print(thing1, ",", thing2)
enter = input("Press ENTER and I will choose your car > ")
if enter == "butt jim":
    print("Just stop...")
    sleep(1)
    print("ShUtTiNg DoWn.?!")
    sleep(3)
    exit(["ERR_BUTT_JIM"])
players = ["Jude M.", "Matthew", "Ian", "William C.", "Zakk"]
cars = ["Diamond Minecart", "HyandAI", "Emerald Car", "Ruby Car", "Cash Cow"]
selection = []
while len(players) != 0:
    player = random.choice(players)
    car = random.choice(cars)
    selection.append((player, car))
    players.remove(player)
    cars.remove(car)
for item in selection:
    print(item)
    sleep(1)