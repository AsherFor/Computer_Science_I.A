from tkinter import *
from matplotlib import pyplot as plt
import numpy as np

master = Tk()
master.title("Golf Statistics")
master.geometry("800x800")
master.configure(background="white")

#Enter Name
Label(master, text='First Name').grid(row=0)
Label(master, text='Last Name').grid(row=1)
first_name = Entry(master)
last_name = Entry(master)
first_name.grid(row=0, column=1)
last_name.grid(row=1, column=1)

#Gets the inpout of the user's name
def get_Input():
    first = first_name.get()
    last = last_name.get()
    print(first,last)
    golf_club = club_name.get()
    print(golf_club)
    raw_distance = [distance.get()]
    print(raw_distance)
    print(type(raw_distance[0]))


Label(master, text='What Club Are You Using?').grid(row=14)
Label(master, text='Enter Distance of Golf Shots').grid(row=15)
club_name = Entry(master)
distance = Entry(master)
club_name.grid(row=14, column=1)
distance.grid(row=15, column=1)



Button(master, text="Submit",command=get_Input).grid(row=5, sticky=W)
Button(master, text="Submit",command=get_Input).grid(row=14, column=2)
Button(master, text="Submit",command=get_Input).grid(row=15, column=2)

master.mainloop()
