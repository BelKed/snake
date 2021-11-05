import tkinter
import time

width = 720
height = 720
x, y = width/2, height/2

size = 20
max_lenght = 10

red, green, blue, gray = "#e36666", "#76e2af", "#32b1d3", "#282c34"

pl = tkinter.Canvas(bg=gray, width=width, height=height)
pl.pack()

coords = [[x, y]]


def draw(event):
    global x, y, size

    tl = event.keysym
    prev_x, prev_y = x, y

    if tl == "Left": x -= size*2
    elif tl == "Right": x += size*2
    elif tl == "Up": y -= size*2
    elif tl == "Down": y += size*2
    else: return

    if (x + size) > width:
        x -= size*2
        blink(x, y)
    elif (x - size*2) < 0:
        x += size*2
        blink(x, y)

    elif (y + size*2) > height:
        y -= size*2
        blink(x, y)
    elif (y - size*2) < 0:
        y += size*2
        blink(x, y)

    else:
        oval(prev_x, prev_y, blue)

        if [x, y] in coords:
            if tl == "Left": x += size*2
            elif tl == "Right": x -= size*2
            elif tl == "Up": y += size*2
            elif tl == "Down": y -= size*2

            blink(x, y)
        else:
            coords.append([x, y])
            oval(x, y, green)

        if len(coords) > max_lenght:
            oval(coords[0][0], coords[0][1], gray)
            coords.remove(coords[0])


def oval(x_oval, y_oval, fill):
    pl.create_rectangle(x_oval - size, y_oval - size, x_oval + size, y_oval + size, fill=fill, width=0)

def blink(x_oval, y_oval):
    oval(x_oval, y_oval, red)
    pl.update()
    time.sleep(0.1)
    oval(x_oval, y_oval, green)
    pl.update()

oval(x, y, green)
pl.bind_all("<Key>", draw)

pl.mainloop()
