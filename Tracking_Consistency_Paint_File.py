from tkinter import *
from tkinter import colorchooser
# Library for taking a screenshot
import pyscreenshot as ImageGrab

master = Tk()

master.title("Tracking Golf Shot Consistency")
master.geometry("750x750")
golf_canvas = Canvas(master, width=700, height=700)

global choose_color;

def paint(tracker):
    global choose_color

    x1, y1, x2, y2 = (tracker.x - 3), (tracker.y - 3), (tracker.x + 3), (tracker.y + 3)

    color = str(choose_color)

    golf_canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)

def color_picker():
    global choose_color
    choose_color = colorchooser.askcolor()[1]

def clear_canvas():
    golf_canvas.delete('all')

def screenshot():
    image = ImageGrab.grab(bbox=(0,0,1600,2100))
    image.show()

#Buttons
Button(master, text="Choose A Color", command=color_picker).grid()
Button(master, text="Clear Canvas", command=clear_canvas).grid()
Button(master, text="Screenshot", command=screenshot).grid()


golf_canvas.bind("<B1-Motion>", paint)

new_label = Label(master, text="First Choose a Color, then Click to Draw.")
new_label.grid()
golf_canvas.grid()

mainloop()