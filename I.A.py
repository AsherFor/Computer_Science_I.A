from tkinter import *
from matplotlib import pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import pandas as pd
# import csv

file = pd.read_csv("Golf_Statistics.csv")


master = Tk()
master.title("Golf Statistics")
master.geometry("700x300")
master.configure(background="white")

#Header of the Program
main_header = Label(master, text = "Golf Statistics")
main_header.config(font =("Times New Roman", 30))
main_header.grid(row=0, column=0)

#Entry for name
Label(master, text='First Name and Last Name').grid(row=2)
name = Entry(master)
name.grid(row=2, column=1)
def name_user():
    entry_name = name.get()
    print(entry_name)

#Entry for Date
Label(master, text='Date').grid(row=3)
date = Entry(master)
date.grid(row=3, column=1)
def date_of_user():
    entry_date = date.get()
    print(entry_date)

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
    Button(newWindow, text="Calculate", command= lambda: claculate_average_distance(distance, club_name)).grid(row=4, column=1)
    # Label and entry for club and distance of golf shots
    Label(newWindow, text='What Club Are You Using?').grid(row=1)
    Label(newWindow, text='Enter Distance of Golf Shots (Ex: 400 + 200 + 100)').grid(row=2)
    club_name = Entry(newWindow)
    distance = Entry(newWindow)
    club_name.grid(row=1, column=1)
    distance.grid(row=2, column=1)

def claculate_average_distance(distance, club_name):
    entry_club_name = club_name.get()
    entry_distance = distance.get()
    count = 0
    # This is a for loop to count the amount of times the + character is in the entry for distance
    for i in entry_distance:
        if i == '+':
            count = count + 1
    count_values = count + 1
    print("You are able to hit your", entry_club_name, "an average distance of", (eval(entry_distance) / count_values), "yards!")

def accuracy_of_shot():
    newWindow = Toplevel(master)
    newWindow.title("Calculate Accuracy")
    newWindow.geometry("600x200")
    #Header
    main_header = Label(newWindow, text="Accuracy of a Golf Club")
    main_header.config(font=("Times New Roman", 20))
    main_header.grid(row=0, column=0)
    #Buttons
    Button(newWindow, text="Graph", command=place_holder).grid(row=3, column=0)
    Button(newWindow, text="Calculate", command= lambda: calculate_accuracy(name_of_club, accuracy)).grid(row=3, column=1)
    #Label and entry for accuracy of a shot
    Label(newWindow, text='What Club Are You Using?').grid(row=1)
    Label(newWindow, text='Enter the type of shot you hit (hook, slice, fade, draw, push, pull').grid(row=2)
    name_of_club = Entry(newWindow)
    accuracy = Entry(newWindow)
    name_of_club.grid(row=1, column=1)
    accuracy.grid(row=2, column=1)

def calculate_accuracy(name_of_club, accuracy):
    entry_name_of_club = name_of_club.get()
    entry_accuracy = accuracy.get()
    print(entry_name_of_club)
    # Counting the amount of occurrences of each type of shot
    Hook = entry_accuracy.count("Hook")
    Slice = entry_accuracy.count("Slice")
    Fade = entry_accuracy.count("Fade")
    Draw = entry_accuracy.count("Draw")
    Push = entry_accuracy.count("Push")
    Pull = entry_accuracy.count("Pull")
    # Calculating the percentage of hitting a certain accuracy shot
    result_hook = (Hook / len(entry_accuracy.split()) * 100)
    result_slice = (Slice / len(entry_accuracy.split()) * 100)
    result_fade = (Fade / len(entry_accuracy.split()) * 100)
    result_draw = (Draw / len(entry_accuracy.split()) * 100)
    result_push = (Push / len(entry_accuracy.split()) * 100)
    result_pull = (Pull / len(entry_accuracy.split()) * 100)
    # Printing result of calculations
    print("You will hit a hook", result_hook, "% of", len(entry_accuracy.split()), "shots!")
    print("You will hit a slice", result_slice, "% of", len(entry_accuracy.split()), "shots!")
    print("You will hit a fade", result_fade, "% of", len(entry_accuracy.split()), "shots!")
    print("You will hit a draw", result_draw, "% of", len(entry_accuracy.split()), "shots!")
    print("You will hit a push", result_push, "% of", len(entry_accuracy.split()), "shots!")
    print("You will hit a pull", result_pull, "% of", len(entry_accuracy.split()), "shots!")

def percentage_chance_of_putt():
    newWindow = Toplevel(master)
    newWindow.title("Calculate Chance of Making a Putt")
    newWindow.geometry("500x200")
    # Header
    main_header = Label(newWindow, text="Chance of Making a Putt")
    main_header.config(font=("Times New Roman", 20))
    main_header.grid(row=0, column=0)
    # Buttons
    Button(newWindow, text="Graph", command=place_holder).grid(row=3, column=0)
    Button(newWindow, text="Calculate", command=lambda: calculate_change_of_putt(length, amount_of_putts)).grid(row=3, column=1)
    # Label and entry for percentage chance of making a putt
    Label(newWindow, text='Length from the hole(10ft, 5ft, 1ft, etc)').grid(row=1)
    Label(newWindow, text='Enter the amount of putts it took to make it into the hole').grid(row=2)
    length = Entry(newWindow)
    amount_of_putts = Entry(newWindow)
    length.grid(row=1, column=1)
    amount_of_putts.grid(row=2, column=1)

def calculate_change_of_putt(length, amount_of_putts):
    entry_length = length.get()
    entry_amount_of_putts = amount_of_putts.get()
    # Counting the amount of putts inputted
    One_Putt = entry_amount_of_putts.count("1")
    Two_Putt = entry_amount_of_putts.count("2")
    Three_Putt = entry_amount_of_putts.count("3")
    Four_Putt = entry_amount_of_putts.count("4")
    Five_Putt = entry_amount_of_putts.count("5")
    Six_Putt = entry_amount_of_putts.count("6")
    Seven_Putt = entry_amount_of_putts.count("7")
    Eight_Putt = entry_amount_of_putts.count("8")
    Nine_Putt = entry_amount_of_putts.count("9")
    Ten_Putt = entry_amount_of_putts.count("10")
    # Calculating the percentages of making a putt
    result_one_putt = (One_Putt / len(entry_amount_of_putts.split()) * 100)
    result_two_putt = (Two_Putt / len(entry_amount_of_putts.split()) * 100)
    result_three_putt = (Three_Putt / len(entry_amount_of_putts.split()) * 100)
    result_four_putt = (Four_Putt / len(entry_amount_of_putts.split()) * 100)
    result_five_putt = (Five_Putt / len(entry_amount_of_putts.split()) * 100)
    result_six_putt = (Six_Putt / len(entry_amount_of_putts.split()) * 100)
    result_seven_putt = (Seven_Putt / len(entry_amount_of_putts.split()) * 100)
    result_eight_putt = (Eight_Putt / len(entry_amount_of_putts.split()) * 100)
    result_nine_putt = (Nine_Putt / len(entry_amount_of_putts.split()) * 100)
    result_ten_putt = (Ten_Putt / len(entry_amount_of_putts.split()) * 100)
    # rinting result of calculations
    print("You will have an", result_one_putt, "% change of making a one putt from", entry_length, "ft away!")
    print("You will have an", result_two_putt, "% change of making a two putt from", entry_length, "ft away!")
    print("You will have an", result_three_putt, "% change of making a three putt from", entry_length, "ft away!")
    print("You will have an", result_four_putt, "% change of making a four putt from", entry_length, "ft away!")
    print("You will have an", result_five_putt, "% change of making a five putt from", entry_length, "ft away!")
    print("You will have an", result_six_putt, "% change of making a six putt from", entry_length, "ft away!")
    print("You will have an", result_seven_putt, "% change of making a seven putt from", entry_length, "ft away!")
    print("You will have an", result_eight_putt, "% change of making a eight putt from", entry_length, "ft away!")
    print("You will have an", result_nine_putt, "% change of making a nine putt from", entry_length, "ft away!")
    print("You will have an", result_ten_putt, "% change of making a ten putt from", entry_length, "ft away!")

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
Label(master, text='Individual notes about golfer').grid(row=8)
notes = Entry(master)
notes.grid(row=8, column=1)
def user_notes():
    entry_notes = notes.get()
    print(entry_notes)

# Function to exit code
def exit_program():
    exit()

#Buttons
Button(master, text="Calculate Average Distance of Golf Club",command=average_distance).grid(row=4)
Button(master, text="Calculate the Accuracy of a Golf Club",command=accuracy_of_shot).grid(row=5)
Button(master, text="Calculate the Percentage Chance of Making a Putt",command=percentage_chance_of_putt).grid(row=6)
Button(master, text="Bird's Eye View of Golf Hole to Track Consistency",command=consistency_graph).grid(row=7)
Button(master, text="Clear",command=place_holder).grid(row=9, column=0)
Button(master, text="Exit",command=exit_program).grid(row=9, column=1)
Button(master, text="Open",command=place_holder).grid(row=9, column=2)
Button(master, text="Download",command=place_holder).grid(row=9, column=3)
Button(master, text="Enter",command=name_user).grid(row=2, column=2)
Button(master, text="Enter",command=date_of_user).grid(row=3, column=2)
Button(master, text="Enter",command=user_notes).grid(row=8, column=2)

master.mainloop()
