import tkinter
import time

size = 20
max_lenght = 10
canvas_size = 720

red, green, blue, gray = "#e36666", "#76e2af", "#32b1d3", "#282c34"
x = y = canvas_size / 2
coords = [[x, y]]

pl = tkinter.Canvas(bg=gray, width=canvas_size, height=canvas_size)
pl.pack()


def draw(event):
    global x, y, size

    tl = event.keysym
    prev_x, prev_y = x, y

    if tl == "Left": x -= size * 2
    elif tl == "Right": x += size * 2
    elif tl == "Up": y -= size * 2
    elif tl == "Down": y += size * 2
    else: return

    if (x + size) > canvas_size:
        x -= size * 2
        blink(x, y)
    elif (x - size * 2) < 0:
        x += size * 2
        blink(x, y)

    elif (y + size * 2) > canvas_size:
        y -= size * 2
        blink(x, y)
    elif (y - size * 2) < 0:
        y += size * 2
        blink(x, y)

    else:
        square(prev_x, prev_y, blue)

        if [x, y] in coords:
            if tl == "Left": x += size * 2
            elif tl == "Right": x -= size * 2
            elif tl == "Up": y += size * 2
            elif tl == "Down": y -= size * 2

            blink(x, y)
        else:
            coords.append([x, y])
            square(x, y, green)

        if len(coords) > max_lenght:
            square(coords[0][0], coords[0][1], gray)
            coords.pop(0)


def square(_x, _y, fill):
    pl.create_rectangle(_x - size, _y - size, _x + size, _y + size, fill=fill, width=0)


def blink(_x, _y):
    square(_x, _y, red)
    pl.update()
    time.sleep(0.1)
    square(_x, _y, green)
    pl.update()


square(x, y, green)
pl.bind_all("<Key>", draw)

pl.mainloop()
