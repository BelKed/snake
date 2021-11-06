import tkinter
import random
import time

snake_size = 20
max_lenght = 10
canvas_size = 720

red, green, blue, gray = "#e36666", "#76e2af", "#32b1d3", "#282c34"
x = y = canvas_size / 2
coords = [[x, y]]

pl = tkinter.Canvas(bg=gray, width=canvas_size, height=canvas_size)
pl.pack()


def draw(event):
    global x, y, snake_size

    tl = event.keysym
    prev_x, prev_y = x, y

    if tl == "Left": x -= snake_size * 2
    elif tl == "Right": x += snake_size * 2
    elif tl == "Up": y -= snake_size * 2
    elif tl == "Down": y += snake_size * 2
    else: return

    if (x + snake_size) > canvas_size:
        x -= snake_size * 2
        blink(x, y)
    elif (x - snake_size * 2) < 0:
        x += snake_size * 2
        blink(x, y)

    elif (y + snake_size * 2) > canvas_size:
        y -= snake_size * 2
        blink(x, y)
    elif (y - snake_size * 2) < 0:
        y += snake_size * 2
        blink(x, y)

    else:
        if [x, y] in coords:
            if tl == "Left": x += snake_size * 2
            elif tl == "Right": x -= snake_size * 2
            elif tl == "Up": y += snake_size * 2
            elif tl == "Down": y -= snake_size * 2

            blink(x, y)
        else:
            coords.append([x, y])
            square(x, y, green)

        if x == fruit_x and y == fruit_y:
            generate_fruit()

        if len(coords) > max_lenght:
            square(coords[0][0], coords[0][1], gray)
            coords.pop(0)

        square(prev_x, prev_y, blue)


def generate_fruit():
    global canvas_size, fruit_x, fruit_y

    fruit_x = random.randrange(snake_size * 2, canvas_size, snake_size * 2)
    fruit_y = random.randrange(snake_size * 2, canvas_size, snake_size * 2)

    circle(fruit_x, fruit_y, red)


def square(_x, _y, fill):
    pl.create_rectangle(_x - snake_size, _y - snake_size, _x + snake_size, _y + snake_size, fill=fill, width=0)


def circle(_x, _y, fill):
    pl.create_oval(_x - snake_size, _y - snake_size, _x + snake_size, _y + snake_size, fill=fill, width=0)


def blink(_x, _y):
    square(_x, _y, red)
    pl.update()
    time.sleep(0.1)
    square(_x, _y, green)
    pl.update()


generate_fruit()
square(x, y, green)

pl.bind_all("<Key>", draw)
pl.mainloop()
