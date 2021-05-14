from tkinter import *
from random import randint
from time import sleep, time
from math import sqrt
w = Tk()
w.title("Bubblator")
w_height = 500
w_width = 800
c = Canvas(w, height = w_height, width = w_width, bg = "black")
c.pack()
def close(event):
    quit()
c.bind_all('<KeyPress-Return>', close)
submarine = c.create_polygon(5,5,5,25,30,15, fill = "red")
submarine2 = c.create_oval(0,0,30,30, outline = "red")
r_submarine = 15
x_center = w_width/2
y_center = w_height/2
c.move(submarine, x_center, y_center)
c.move(submarine2, x_center, y_center)
speed_submarine = 10
def move_submarine(event):
    key = event.keysym
    if key == "Up":
        c.move(submarine, 0, -speed_submarine)
        c.move(submarine2, 0, -speed_submarine)
    if key == "Down":
        c.move(submarine, 0, speed_submarine)
        c.move(submarine2, 0, speed_submarine)
    if key == "Left":
        c.move(submarine, -speed_submarine, 0)
        c.move(submarine2, -speed_submarine, 0)
    if key == "Right":
        c.move(submarine, speed_submarine, 0)
        c.move(submarine2, speed_submarine, 0)
c.bind_all('<Key>', move_submarine)
id_bubble = list ()
r_bubble = list()
speed_bubble = list()
r_bubble_min = 10
r_bubble_max = 30
speed_bubble_max = 30
gap = 100
def create_bubble():
    x = w_width + gap
    y = randint(0, w_height)
    r = randint(r_bubble_min, r_bubble_max)
    id1 = c.create_oval(x-r, y-r, x+r, y+r, outline = "white")
    id_bubble.append(id1)
    r_bubble.append(r)
    speed_bubble.append(randint(1, speed_bubble_max))
def move_bubble():
    for i in range(len(id_bubble)):
        c.move(id_bubble[i], -speed_bubble[i], 0)
def find_coords(num_id):
    pos = c.coords(num_id)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/2
    return x,y
def del_bubble(i):
    del r_bubble[i]
    del speed_bubble[i]
    c.delete(id_bubble[i])
    del id_bubble[i]
def erase_bubbles():
    for i in range(len(id_bubble)-1, -1, -1):
        x, y = find_coords(id_bubble[i])
        if x < -gap:
            del_bubble(i)
def distance(id1, id2):
    x1, y1 = find_coords(id1)
    x2, y2 = find_coords(id2)
    return sqrt((x2-x1)**2 + (y2-y1)**2)
def collision():
    points = 0
    for bubble in range(len(id_bubble)-1, -1, -1):
        if distance(submarine2, id_bubble[bubble]) < (r_submarine + r_bubble[bubble]):
            points += (r_bubble[bubble] + speed_bubble[bubble])
            del_bubble(bubble)
    return points
c.create_text(100, 30, text = "TIME LEFT", fill = "white")
c.create_text(200, 30, text = "SCORE", fill = "white")
text_time = c.create_text(100, 50, fill = "white")
text_score = c.create_text(200, 50, fill = "white")
def show_score(score):
    c.itemconfig(text_score, text = str(score))
def show_time(time_left):
    c.itemconfig(text_time, text = str(time_left))
bubble_random = 10
time_limit = 30
score_bonus = 1000
score = 10
bonus = 0
end = time() + time_limit
while time() < end:
    if randint(1, bubble_random) == 1:
        create_bubble()
    move_bubble()
    erase_bubbles()
    score += collision()
    if (int(score/score_bonus)):
        bonus += 1
        end += time_limit
    show_score(score)
    show_time(int(end-time()))
    w.update()
    sleep(0.01)
c.create_text(x_center, y_center, text = "END OF GAME", fill = "white", font =("Helvetica", 30))
c.create_text(x_center, y_center+30, text = "Score: " +str(score), fill = "white")
c.create_text(x_center, y_center+45, text = "Bonus Time: " +str(bonus*time_limit), fill = "white")
