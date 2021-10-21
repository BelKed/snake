import tkinter

pl = tkinter.Canvas(bg='blue', width=800, height=600)
pl.pack()

xt, yt = 400, 50
x, y, r = 400, 300, 10

pl.create_oval(x - r, y - r, x + r, y + r, fill='yellow', outline='red', width=5)

coords = [[x, y]]


def kresli(event):
    global x, y, r

    tl = event.keysym

    prev_x = x
    prev_y = y

    if tl == 'Left':
        x -= r*2

    elif tl == 'Right':
        x += r*2

    elif tl == 'Up':
        y -= r*2

    elif tl == 'Down':
        y += r*2

    color = 'red'
    if ([x, y] in coords):
        color = 'blue'
    else:
        coords.append([x, y])

    pl.create_oval(x - r, y - r, x + r, y + r, fill=color, outline='red', width=5)
    pl.create_oval(prev_x - r, prev_y - r, prev_x + r, prev_y + r, fill='yellow', outline='red', width=5)


pl.bind_all('<Key>', kresli)

pl.mainloop()
