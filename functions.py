from turtle import Turtle
from time import sleep
name = input("Whats your name? > ")
kappa = Turtle()
kappa.begin_fill()
def square(side, color, x, y):
    kappa.penup()
    kappa.goto(x, y)
    kappa.pendown()
    for i in range(4):
        kappa.color(color)
        kappa.pencolor(color)
        kappa.fillcolor(color)
        kappa.forward(side)
        kappa.left(90)
square(200, "cyan", 100, 40)
kappa.end_fill()
kappa.penup()
kappa.hideturtle()
kappa.goto(-300, 0)
kappa.pendown()
kappa.showturtle()
kappa.begin_fill()
def rectangle(side1, side2, color):
    for i in range(2):
        kappa.fillcolor(color)
        kappa.color(color)
        kappa.pencolor(color)
        kappa.forward(side1)
        kappa.right(90)
        kappa.forward(side2)
        kappa.right(90)
rectangle(200, 70, "black")
kappa.end_fill()
kappa.penup()
kappa.hideturtle()
kappa.goto(300, 0)
kappa.pendown()
kappa.showturtle()
kappa.begin_fill()
def triangle(side, color):
    for i in range(3):
        kappa.color(color)
        kappa.pencolor(color)
        kappa.fillcolor(color)
        kappa.forward(side)
        kappa.right(120)
triangle(200, "green")
kappa.end_fill()
kappa.hideturtle()
print("It is done!!!!!!!!!!!!!!!")
sleep(1)
print("I drew a gold square...")
sleep(1)
print("A green rectangle...")
sleep(1)
print("and a blue triangle!!!!!!!!!!!!")
sleep(1)
print("Thanks for trying it,", name)
sleep(30)