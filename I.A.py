from tkinter import *
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
# import csv

Csv_file = "Golf Statistics"

master = Tk()
master.title("Golf Statistics")
master.geometry("500x500")
master.configure(background="white")

#Header of the Program
main_header = Label(master, text = "Golf Statistics")
main_header.config(font =("Times New Roman", 30))
main_header.grid(row=0, column=0)

#Entry for name and date
Label(master, text='First Name and Last Name').grid(row=2)
name = Entry(master)
name.grid(row=2, column=1)

def average_distance():
    newWindow = Toplevel(master)
    newWindow.title("Calculate Average Distance")
    newWindow.geometry("600x200")
    #Header
    main_header = Label(newWindow, text="Average Distance of a Golf Club")
    main_header.config(font=("Times New Roman", 20))
    main_header.grid(row=0, column=0)
    #Buttons
    Button(newWindow, text="Graph", command=place_holder).grid(row=3, column=0)
    Button(newWindow, text="Calculate", command=place_holder).grid(row=4, column=1)
    # Label and entry for club and distance of golf shots
    Label(newWindow, text='What Club Are You Using?').grid(row=1)
    Label(newWindow, text='Enter Distance of Golf Shots').grid(row=2)
    club_name = Entry(newWindow)
    distance = Entry(newWindow)
    club_name.grid(row=1, column=1)
    distance.grid(row=2, column=1)

def accuracy_of_shot():
    newWindow = Toplevel(master)
    newWindow.title("Calculate Average Distance")
    newWindow.geometry("600x200")
    #Header
    main_header = Label(newWindow, text="Accuracy of a Golf Club")
    main_header.config(font=("Times New Roman", 20))
    main_header.grid(row=0, column=0)
    #Buttons
    Button(newWindow, text="Graph", command=place_holder).grid(row=3, column=0)
    Button(newWindow, text="Calculate", command=place_holder).grid(row=3, column=1)
    #Label and entry for accuracy of a shot
    Label(newWindow, text='What Club Are You Using?').grid(row=1)
    Label(newWindow, text='Enter the type of shot you hit (hook, slice, fade, draw, push, pull').grid(row=2)
    name_of_club = Entry(newWindow)
    accuracy = Entry(newWindow)
    name_of_club.grid(row=1, column=1)
    accuracy.grid(row=2, column=1)

def percentage_chance_of_putt():
    newWindow = Toplevel(master)
    newWindow.title("Calculate Average Distance")
    newWindow.geometry("500x200")
    # Header
    main_header = Label(newWindow, text="Chance of Making a Putt")
    main_header.config(font=("Times New Roman", 20))
    main_header.grid(row=0, column=0)
    # Buttons
    Button(newWindow, text="Graph", command=place_holder).grid(row=3, column=0)
    Button(newWindow, text="Calculate", command=place_holder).grid(row=3, column=1)
    # Label and entry for percentage chance of making a putt
    Label(newWindow, text='Length from the hole(10ft, 5ft, 1ft, etc)').grid(row=1)
    Label(newWindow, text='Enter the Amount of putts it took to make it into the hole').grid(row=2)
    length = Entry(newWindow)
    amount_of_putts = Entry(newWindow)
    length.grid(row=1, column=1)
    amount_of_putts.grid(row=2, column=1)

def consistency_graph():
    fig, ax = plt.subplots()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    arr_lena = mpimg.imread('GolfHole.png')
    imagebox = OffsetImage(arr_lena, zoom=0.2)
    ab = AnnotationBbox(imagebox, (0.4, 0.6))
    ax.add_artist(ab)
    plt.grid()
    plt.draw()
    plt.savefig('add_picture_matplotlib_figure.png', bbox_inches='tight')
    plt.show()

#Place holder function for graphs
def place_holder():
    print("hi")

#Individual notes about golfer
Label(master, text='Individual notes about golfer').grid(row=7)
notes = Entry(master)
notes.grid(row=7, column=1)

#Buttons
Button(master, text="Calculate Average Distance of Golf Club",command=average_distance).grid(row=3)
Button(master, text="Calculate the Accuracy of a Golf Club",command=accuracy_of_shot).grid(row=4)
Button(master, text="Calculate the Percentage Chance of Making a Putt",command=percentage_chance_of_putt).grid(row=5)
Button(master, text="Bird's Eye View of Golf Hole to Track Consistency",command=consistency_graph).grid(row=6)
Button(master, text="Clear",command=place_holder).grid(row=9, column=0)
Button(master, text="Exit",command=place_holder).grid(row=9, column=1)
Button(master, text="Open",command=place_holder).grid(row=9, column=2)
Button(master, text="Download",command=place_holder).grid(row=9, column=3)


#Submit Buttons
# Button(master, text="Submit",command=get_Input).grid(row=0, column=2)
# Button(master, text="Submit",command=get_Input).grid(row=14, column=2)
# Button(master, text="Submit",command=get_Input).grid(row=15, column=2)
# Button(master, text="Submit",command=get_Input).grid(row=16, column=2)
# Button(master, text="Submit",command=get_Input).grid(row=17, column=2)
# Button(master, text="Submit",command=get_Input).grid(row=18, column=2)
# Button(master, text="Submit",command=get_Input).grid(row=19, column=2)

master.mainloop()


