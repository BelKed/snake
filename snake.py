import tkinter
import random
import time

snake_size = 20
max_lenght = 10
canvas_size = 720

red, green, blue, gray = "#e36666", "#76e2af", "#32b1d3", "#282c34"
current_x = current_y = canvas_size / 2
coords = [[current_x, current_y]]
score = score_element = 0

pl = tkinter.Canvas(bg=gray, width=canvas_size, height=canvas_size)
pl.pack()


def draw(event):
    global current_x, current_y, snake_size, score

    tl = event.keysym
    prev_x, prev_y = current_x, current_y

    if tl == "Left": current_x -= snake_size * 2
    elif tl == "Right": current_x += snake_size * 2
    elif tl == "Up": current_y -= snake_size * 2
    elif tl == "Down": current_y += snake_size * 2
    else: return

    if (current_x + snake_size * 2) > canvas_size:
        current_x -= snake_size * 2
        blink(current_x, current_y)
    elif (current_x - snake_size * 2) < 0:
        current_x += snake_size * 2
        blink(current_x, current_y)

    elif (current_y + snake_size * 2) > canvas_size:
        current_y -= snake_size * 2
        blink(current_x, current_y)
    elif (current_y - snake_size * 2) < 0:
        current_y += snake_size * 2
        blink(current_x, current_y)

    else:
        if [current_x, current_y] in coords:
            if tl == "Left": current_x += snake_size * 2
            elif tl == "Right": current_x -= snake_size * 2
            elif tl == "Up": current_y += snake_size * 2
            elif tl == "Down": current_y -= snake_size * 2

            blink(current_x, current_y)
        else:
            coords.append([current_x, current_y])
            square(current_x, current_y, green)

        if current_x == fruit_x and current_y == fruit_y:
            score += 1
            generate_fruit()

        if len(coords) > score + 2:
            square(coords[0][0], coords[0][1], gray)
            coords.pop(0)

        square(prev_x, prev_y, blue)
        print_score(score)


def generate_fruit():
    global canvas_size, fruit_x, fruit_y

    fruit_x = random.randrange(snake_size * 2, canvas_size, snake_size * 2)
    fruit_y = random.randrange(snake_size * 2, canvas_size, snake_size * 2)

    circle(fruit_x, fruit_y, red)


def square(_x, _y, fill):
    return pl.create_rectangle(_x - snake_size, _y - snake_size, _x + snake_size, _y + snake_size, fill=fill, width=0)


def circle(_x, _y, fill):
    return pl.create_oval(_x - snake_size, _y - snake_size, _x + snake_size, _y + snake_size, fill=fill, width=0)


def blink(_x, _y):
    square(_x, _y, red)
    pl.update()
    time.sleep(0.1)
    square(_x, _y, green)
    pl.update()


def print_score(text):
    global score_element

    pl.delete(score_element)
    score_element = pl.create_text(canvas_size / 2, 40, fill="yellow", text=text, font=("JetBrains Mono", 30, "bold"))


print_score(score)
generate_fruit()
square(current_x, current_y, green)

pl.bind_all("<Key>", draw)
pl.mainloop()
