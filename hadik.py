import tkinter

width = 800
height = 800
x, y, r = width/2, height/2, 20

pl = tkinter.Canvas(bg='gray', width=width, height=height)
pl.pack()

pl.create_oval(x - r, y - r, x + r, y + r, fill='yellow', outline='red', width=5)

coords = [[x, y]]


def kresli(event):
    global x, y, r, prev_x, prev_y
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

    if (x + r) > width:
        x -= 2*r
        oval(prev_x, prev_y, 'red')
        pl.after(200, oval, x, y, 'orange')
    elif (x - 2*r) < 0:
        x += 2*r
        oval(prev_x, prev_y, 'red')
        pl.after(200, oval, x, y, 'orange')

    elif (y + 2*r) > height:
        y -= 2*r
        oval(prev_x, prev_y, 'red')
        pl.after(200, oval, x, y, 'orange')
    elif (y - 2*r) < 0:
        y += 2*r
        oval(prev_x, prev_y, 'red')
        pl.after(200, oval, x, y, 'orange')

    else:
        if ([x, y] in coords):
            oval(x, y, 'red')
            pl.after(200, oval, x, y, 'blue')
            oval(prev_x, prev_y, 'yellow')
        else:
            oval(x, y, 'orange')
            oval(prev_x, prev_y, 'yellow')
            coords.append([x, y])


def oval(x_oval, y_oval, fill, outline='red'):
    pl.create_oval(x_oval - r, y_oval - r, x_oval + r, y_oval + r, fill=fill, outline=outline, width=r/4)


pl.bind_all('<Key>', kresli)

pl.mainloop()
