from tkinter import *
from random import randint,choice
size = 800
window = Tk()
canvas = Canvas(window, width = size, height = size)
canvas.pack()
rect1 = canvas.create_rectangle(100,100,300,200, outline = "red", fill = "pink")
rect2 = canvas.create_rectangle(400,150,650,200, outline = "orange", fill = "blue")
rect3 = canvas.create_rectangle(300,300,400,400, outline = "pink", fill = "red")
oval1 = canvas.create_oval(200,550,600,650, fill = "yellow")
oval2 = canvas.create_oval(150,100,250,200, fill = "black")
triangle1 = canvas.create_polygon(400,100,525,50,650,100, fill = "green")