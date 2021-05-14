from tkinter import *
window = Tk()
window.attributes("-topmost", 1)
window.title("JARVIS Alien")
canvas = Canvas(window, height = 300, width = 400)
canvas.pack()
body = canvas.create_oval(100,150,300,250, fill = "green")
eye = canvas.create_oval(170,70,230,130, fill = "white")
pupil = canvas.create_oval(190,90,210,110, fill = "black")
mouth = canvas.create_oval(150,220,250,240, fill = "red")
neck = canvas.create_line(200,150,200,130, width = 5)
hat = canvas.create_polygon(180,75,220,75,200,20, fill = "blue")
words = canvas.create_text(320,250,text="My name is JARVIS!")
def open_mouth():
    canvas.itemconfig(mouth, fill="black")nvas.bind_all("<KeyPress-\>", not_stolen_hat)
  File "/usr/lib/python3.7/tkinter/__init__.py", line 1263, in bind_all
    return self._bind(('bind', 'all'), sequence, func, add, 0)
  File "/usr/lib/python3.7/tkinter/__init__.py", line 1206, in _bind
    self.tk.call(what + (sequence, cmd))
def close_mouth():
    canvas.itemconfig(mouth, fill="red")
    canvas.itemconfig(words, text="My name is JARVIS!")
def open_eye():
    canvas.itemconfig(eye, fill="green")
    canvas.itemconfig(pupil, state=HIDDEN)
def close_eye():
    canvas.itemconfig(eye, fill = "white")
    canvas.itemconfig(pupil, state=NORMAL)
def stolen_hat():
    canvas.itemconfig(hat, state=HIDDEN)
    canvas.itemconfig(words, text = "Give me back my stupid looking hat!!!!")
def not_stolen_hat():
    canvas.itemconfig(hat, state=NORMAL)
    canvas.itemconfig(words, text = "My name is JARVIS!")
def burp(event):
    open_mouth()
    canvas.itemconfig(words, text = "Burp!!!")
canvas.bind_all('<Button-1>', burp)
def open_eye(event):
    canvas.itemconfig(eye, fill="green")
    canvas.itemconfig(pupil, state=HIDDEN)
def close_eye(event):
    canvas.itemconfig(eye, fnvas.bind_all("<KeyPress-\>", not_stolen_hat)
  File "/usr/lib/python3.7/tkinter/__init__.py", line 1263, in bind_all
    return self._bind(('bind', 'all'), sequence, func, add, 0)
  File "/usr/lib/python3.7/tkinter/__init__.py", line 1206, in _bind
    self.tk.call(what + (sequence, cmd))ill = "white")
    canvas.itemconfig(pupil, state=NORMAL)
canvas.bind_all("<KeyPress-a>", open_eye)
canvas.bind_all("<KeyPress-z>", close_eye)
def control_pupil(event):
    key = event.keysym
    if key == "Up":
        canvas.move(pupil, 0, -1)
    elif key == "Down":
        canvas.move(pupil, 0, 1)
    elif key == "Left":
        canvas.move(pupil, -1, 0)
    elif key == "Right":
        canvas.move(pupil, 1, 0)
canvas.bind_all("<Key>", control_pupil)
def stolen_hat(event):
    canvas.itemconfig(hat, state=HIDDEN)
    canvas.itemconfig(words, text = "Give me back my stupid looking hat!!!!")
canvas.bind_all("<KeyPress-Return>", stolen_hat)
def not_stolen_hat(event):
    canvas.itemconfig(hat, state=NORMAL)
    canvas.itemconfig(words, text = "My name is JARVIS!")
canvas.bind_all("<KeyPress-/>", not_stolen_hat)
def close_mouth(event):
    canvas.itemconfig(mouth, fill="red")
    canvas.itemconfig(words, text="My name is JARVIS!")
canvas.bind_all('<Button-3>', close_mouth)