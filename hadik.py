import tkinter
import time

width = 720
height = 720
x, y, r = width/2, height/2, 20

pl = tkinter.Canvas(bg="#282c34", width=width, height=height)
pl.pack()

coords = [[x, y]]


def kresli(event):
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
        x -= 2*r
        oval(prev_x, prev_y, "#e74c3c")
        pl.update()
        time.sleep(0.2)
        oval(x, y, "#76e2af")
        pl.update()
    elif (x - 2*r) < 0:
        x += 2*r
        oval(prev_x, prev_y, "#e74c3c")
        pl.update()
        time.sleep(0.2)
        oval(x, y, "#76e2af")
        pl.update()

    elif (y + 2*r) > height:
        y -= 2*r
        oval(prev_x, prev_y, "#e74c3c")
        pl.update()
        time.sleep(0.2)
        oval(x, y, "#76e2af")
        pl.update()
    elif (y - 2*r) < 0:
        y += 2*r
        oval(prev_x, prev_y, "#e74c3c")
        pl.update()
        time.sleep(0.2)
        oval(x, y, "#76e2af")
        pl.update()

    else:
        oval(prev_x, prev_y, "#32b1d3")
        if ([x, y] in coords):
            oval(x, y, "#e74c3c")
            pl.update()
            time.sleep(0.2)
            oval(x, y, "#76e2af")
            pl.update()
        else:
            oval(x, y, "#76e2af")
            oval(prev_x, prev_y, "#32b1d3")
            coords.append([x, y])


def oval(x_oval, y_oval, fill):
    pl.create_rectangle(x_oval - r, y_oval - r, x_oval + r, y_oval + r, fill=fill, width=0)


oval(x, y, "#76e2af")
pl.bind_all("<Key>", kresli)

pl.mainloop()
