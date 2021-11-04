from tkinter import *
from tkinter import colorchooser
# Library for taking a screenshot
import pyscreenshot as ImageGrab
import pyautogui

master = Tk()

# Creates GUI
master.title("Tracking Golf Shot Consistency")
master.geometry("750x750")
golf_canvas = Canvas(master, width=700, height=700)

global choose_color;


# Function to paint with mouse pointer
def paint(tracker):
    global choose_color

    x1, y1, x2, y2 = (tracker.x - 3), (tracker.y - 3), (tracker.x + 3), (tracker.y + 3)

    color = str(choose_color)

    golf_canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)


# Function to choose a color
def color_picker():
    global choose_color
    choose_color = colorchooser.askcolor()[1]


# Function to clear the canvas
def clear_canvas():
    golf_canvas.delete('all')


# Function to take a screenshot
def screenshot():
    myScreenshot = pyautogui.screenshot()
    myScreenshot.show()
    # image = ImageGrab.grab()
    # image.show()


#Buttons
Button(master, text="Choose A Color", command=color_picker).grid()
Button(master, text="Clear Canvas", command=clear_canvas).grid()
Button(master, text="Screenshot", command=screenshot).grid()

golf_canvas.bind("<B1-Motion>", paint)

new_label = Label(master, text="First Choose a Color, then Click to Draw.")
new_label.grid()
golf_canvas.grid()

mainloop()