from turtle import Turtle
kappa = Turtle()
def star(color):
    kappa.color(color)
    kappa.pencolor(color)
    kappa.fillcolor(color)
    for i in range(5):
        kappa.forward(100)
        kappa.right(144)
def triangle(color):
    kappa.penup()
    kappa.goto(100, 0)
    kappa.pendown()
    kappa.color(color)
    kappa.pencolor(color)
    kappa.fillcolor(color)
    kappa.begin_fill()
    for i in range(3):
        kappa.forward(100)
        kappa.left(120)
    kappa.end_fill()

star("green")
triangle("cyan")