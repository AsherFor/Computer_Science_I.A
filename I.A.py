from tkinter import *
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox\
# import csv

Csv_file = "Golf Statistics"

master = Tk()
master.title("Golf Statistics")
master.geometry("800x800")
master.configure(background="white")


def average_distance():
    newWindow = Toplevel(master)
    newWindow.title("Calculate Average Distance")
    newWindow.geometry("400x200")
    Button(newWindow, text="Graph", command=get_Input).grid(row=3, column=0)
    # Label and entry for club and distance of golf shots
    Label(newWindow, text='What Club Are You Using?').grid(row=1)
    Label(newWindow, text='Enter Distance of Golf Shots').grid(row=2)
    club_name = Entry(newWindow)
    distance = Entry(newWindow)
    club_name.grid(row=1, column=1)
    distance.grid(row=2, column=1)

#Label and entry for name
Label(master, text='Enter first name and last name').grid(row=0)
name = Entry(master)
name.grid(row=0, column=1)

#Label and entry to calculate average distance
Button(master, text="Calculate Average Distance of Golf Club",command=average_distance).grid(row=1)
Button(master, text="Calculate the Accuracy of a Golf Club",command=average_distance).grid(row=2)
Button(master, text="Calculate the Percentage Chance of Making a Putt",command=average_distance).grid(row=3)

#Gets the inpout of the user's name
def get_Input():
    print("hi")
    # full_name = name.get()
    # print(full_name)
    # golf_club = club_name.get()
    # print(golf_club)
    #
    # raw_distance = distance.get()
    # int_raw_distance = int(raw_distance)
    # pie_chart = [int_raw_distance]
    # print(pie_chart)

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



#Label and entry for accuracy of a shot
Label(master, text='What Club Are You Using?').grid(row=16)
Label(master, text='Enter the type of shot you hit (hook, slice, fade, draw, push, pull').grid(row=17)
name_of_club = Entry(master)
accuracy = Entry(master)
name_of_club.grid(row=16, column=1)
accuracy.grid(row=17, column=1)

#Label and entry for percentage chance of making a putt
Label(master, text='Length from the hole(10ft, 5ft, 1ft, etc)').grid(row=18)
Label(master, text='Enter the Amount of putts it took to make it into the hole').grid(row=19)
length = Entry(master)
amount_of_putts = Entry(master)
length.grid(row=18, column=1)
amount_of_putts.grid(row=19, column=1)


#Submit Buttons
Button(master, text="Submit",command=get_Input).grid(row=0, column=2)
Button(master, text="Submit",command=get_Input).grid(row=14, column=2)
Button(master, text="Submit",command=get_Input).grid(row=15, column=2)
Button(master, text="Submit",command=get_Input).grid(row=16, column=2)
Button(master, text="Submit",command=get_Input).grid(row=17, column=2)
Button(master, text="Submit",command=get_Input).grid(row=18, column=2)
Button(master, text="Submit",command=get_Input).grid(row=19, column=2)

#Graph Buttons
Button(master, text="Graph",command=get_Input).grid(row=15, column=3)
Button(master, text="Graph",command=get_Input).grid(row=17, column=3)
Button(master, text="Graph",command=average_distance).grid(row=19, column=3)

#Visual Accuracy of a Golf Shot
Button(master, text="Bird's Eye View of Golf Hole to Track Consistency",command=consistency_graph).grid(row=20)


master.mainloop()
