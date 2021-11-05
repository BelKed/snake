import tkinter
import time

width = 720
height = 720
x, y, r = width/2, height/2, 20

max_lenght = 10

red, green, blue, gray = "#e36666", "#76e2af", "#32b1d3", "#282c34"

pl = tkinter.Canvas(bg=gray, width=width, height=height)
pl.pack()

coords = [[x, y]]


def draw(event):
    global x, y, r
    tl = event.keysym

    prev_x, prev_y = x, y

    if tl == "Left": x -= r*2
    elif tl == "Right": x += r*2
    elif tl == "Up": y -= r*2
    elif tl == "Down": y += r*2

    if (x + r) > width:
        x -= r*2
        blink(x, y)
    elif (x - r*2) < 0:
        x += r*2
        blink(x, y)

    elif (y + r*2) > height:
        y -= r*2
        blink(x, y)
    elif (y - r*2) < 0:
        y += r*2
        blink(x, y)

    else:
        oval(prev_x, prev_y, blue)

        if [x, y] in coords:
            blink(x, y)
            coords.remove([x, y])
        else:
            oval(x, y, green)

        coords.append([x, y])
        
        if len(coords) > max_lenght:
            oval(coords[0][0], coords[0][1], gray)
            coords.remove(coords[0])

        oval(prev_x, prev_y, blue)


def oval(x_oval, y_oval, fill):
    pl.create_rectangle(x_oval - r, y_oval - r, x_oval + r, y_oval + r, fill=fill, width=0)

def blink(x_oval, y_oval):
    oval(x_oval, y_oval, red)
    pl.update()
    time.sleep(0.1)
    oval(x_oval, y_oval, green)
    pl.update()

oval(x, y, green)
pl.bind_all("<Key>", draw)

pl.mainloop()
