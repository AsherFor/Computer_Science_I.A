from tkinter import *

master = Tk()

master.title("Tracking Golf Shot Consistency")
master.geometry("750x750")

def paint(event):
    x1, y1, x2, y2 = (event.x - 3), (event.y - 3), (event.x + 3), (event.y + 3)

    Colour = "#000000"

    w.create_line(x1, y1, x2, y2, fill=Colour)


w = Canvas(master, width=750, height=750)
w.bind("<B1-Motion>", paint)

l = Label(master, text="Double Click and Drag to draw.")
l.pack()
w.pack()

mainloop()