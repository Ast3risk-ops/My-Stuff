from tkinter import *
window = Tk() #create a window
window.attributes("-topmost", 1)
def action_bA():
    print("Thank you")
def action_bB():
    print("Wrong Button")
buttonA = Button(window, text = "Press here!", command = action_bA)
buttonB = Button(window, text = "Do not press here!", command = action_bB)
buttonA.pack()
buttonB.pack()