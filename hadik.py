import tkinter
import time

width = 720
height = 720
x, y, r = width/2, height/2, 20

red, green, blue, gray = "#e74c3c", "#76e2af", "#32b1d3", "#282c34"

pl = tkinter.Canvas(bg=gray, width=width, height=height)
pl.pack()

coords = [[x, y]]


def draw(event):
    global x, y, r, prev_x, prev_y
    tl = event.keysym

    prev_x = x
    prev_y = y

    if tl == "Left":
        x -= r*2
    elif tl == "Right":
        x += r*2
    elif tl == "Up":
        y -= r*2
    elif tl == "Down":
        y += r*2

    if (x + r) > width:
        x -= r*2
        oval(x, y, red)
        pl.update()
        time.sleep(0.2)
        oval(x, y, green)
        pl.update()
    elif (x - r*2) < 0:
        x += r*2
        oval(x, y, red)
        pl.update()
        time.sleep(0.2)
        oval(x, y, green)
        pl.update()

    elif (y + r*2) > height:
        y -= r*2
        oval(x, y, red)
        pl.update()
        time.sleep(0.2)
        oval(x, y, green)
        pl.update()
    elif (y - r*2) < 0:
        y += r*2
        oval(x, y, red)
        pl.update()
        time.sleep(0.2)
        oval(x, y, green)
        pl.update()

    else:
        oval(prev_x, prev_y, blue)
        if ([x, y] in coords):
            oval(x, y, red)
            pl.update()
            time.sleep(0.2)
            oval(x, y, green)
            pl.update()
        else:
            oval(x, y, green)
            coords.append([x, y])

        oval(prev_x, prev_y, blue)


def oval(x_oval, y_oval, fill):
    pl.create_rectangle(x_oval - r, y_oval - r, x_oval + r, y_oval + r, fill=fill, width=0)


oval(x, y, green)
pl.bind_all("<Key>", draw)

pl.mainloop()
