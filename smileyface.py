from time import sleep
from turtle import done
name = input("What is your name? > ")
input("Press return to see a smiley face")
print("Hold on the window border to pause and release to resume")
sleep(3)
from turtle import Turtle
Kappa = Turtle()
Kappa.color("gold")
Kappa.hideturtle()
# Drawing the circle for the head in yellow
Kappa.penup()
Kappa.goto(0, -300)
Kappa.pendown()
Kappa.pencolor("gold")
Kappa.fillcolor("gold")
Kappa.showturtle()
Kappa.begin_fill()
Kappa.circle(300)
Kappa.end_fill()
Kappa.penup()
# Drawing the first eye in blue
Kappa.goto(-140, 80)
Kappa.pendown()
Kappa.pencolor("blue")
Kappa.color("blue")
Kappa.fillcolor("blue")
Kappa.begin_fill()
Kappa.circle(40)
Kappa.end_fill()
Kappa.penup()
# Drawing the second eye
Kappa.hideturtle()
Kappa.goto(140, 80)
Kappa.pendown()
Kappa.showturtle()
Kappa.begin_fill()
Kappa.circle(40)
Kappa.end_fill()
Kappa.color("black")
Kappa.pencolor("black")
# Doing the smile
Kappa.width(40)
Kappa.hideturtle()
Kappa.penup()
Kappa.goto(-200, -60)
Kappa.pendown()
Kappa.showturtle()
Kappa.goto(-140, -140)
Kappa.goto(-80, -180)
Kappa.goto(0, -200)
Kappa.goto(80, -180)
Kappa.goto(140, -140)
Kappa.goto(200,-60)
Kappa.hideturtle()
Kappa.penup()
Kappa.goto(0, 0)
Kappa.pendown()
done()
print("the smiley face is done!!!!!!!!!!!!!")
print("Type yes or no")
like = input(" Do you like it? > ")
if like == "yes":
    print("That's great!!!!!!!!!!!!!")
    print("Thanks,", name)
else:
    print("Oh, you don't like it?")
    print("Thats ok")
    print("But thanks for trying it out,", name)

sleep(30)