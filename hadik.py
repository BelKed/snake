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

    if tl == 'Left':
        x -= r*2

    if tl == 'Right':
        x += r*2

    if tl == 'Up':
        y -= r*2

    if tl == 'Down':
        y += r*2

    color = 'yellow'
    if ([x, y] in coords):
        color = 'blue'
    else:
        coords.append([x, y])

    pl.create_oval(x - r, y - r, x + r, y + r, fill=color, outline='red', width=5)


pl.bind_all('<Key>', kresli)

pl.mainloop()
