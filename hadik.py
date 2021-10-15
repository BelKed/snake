# dokoncit hadika (prechod -> zmena kruzku)

import tkinter

pl = tkinter.Canvas(bg='blue', width=800, height=600)
pl.pack()

xt, yt = 400, 50
x, y, r = 400, 300, 10

pl.create_oval(x - r, y - r, x + r, y + r, fill='yellow', outline='red', width=5)
pl.create_text(xt, yt, fill='yellow', text='KUK', font='Arial 30', angle=45)

def kresli(event):
    global x, y, r

    # pl.delete('all')

    tl = event.keysym
    print(tl)

    if tl == 'Left':
        x -= r*2

    if tl == 'Right':
        x += r*2

    if tl == 'Up':
        y -= r*2

    if tl == 'Down':
        y += r*2

    pl.create_oval(x - r, y - r, x + r, y + r, fill='yellow', outline='red', width=5)

pl.bind_all('<Key>', kresli)

pl.mainloop()
