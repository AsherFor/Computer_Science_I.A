from tkinter import *
from matplotlib import pyplot as plt
# from PIL import Image, ImageTK
# import matplotlib.image as mpimg
import numpy as np
# from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import pandas as pd
import runpy
import csv
import xlsxwriter
from openpyxl import Workbook

#
# writer2 = pd.ExcelWriter('Golf_Statistics.xlsx')
#
#
# df_1 = pd.DataFrame()
# df_2 = pd.DataFrame()
# df_3 = pd.DataFrame()
#
# df_1.to_excel(writer2, sheet_name = 'Average Distance of Golf Club', index = False)
# df_2.to_excel(writer2, sheet_name = 'Accuracy of a Golf Club', index = False)
# df_3.to_excel(writer2, sheet_name = '% Chance of Making a Putt', index = False)
#
#
# writer2.save()


# Creates an excel file
# Creating a workbook and three sheets

wb = Workbook()
sheet1 = wb.active
sheet1.title = "Average Distance of Golf Club"

column_titles_sheet1 = ['Name', 'Date', 'Notes', 'Driver', '3-Wood', '5-Wood', '3-Iron',
                        '4-Iron', '5-Iron', '6-Iron', '7-Iron', '8-Iron', '9-Iron', 'Pitching Wedge', 'Gap Wdge', 'Sand Wedge', 'Lob Wedge', 'Putter']

sheet1['A1'] = column_titles_sheet1[0]
sheet1['B1'] = column_titles_sheet1[1]
sheet1['C1'] = column_titles_sheet1[2]
sheet1['D1'] = column_titles_sheet1[3]
sheet1['E1'] = column_titles_sheet1[4]
sheet1['F1'] = column_titles_sheet1[5]
sheet1['G1'] = column_titles_sheet1[6]
sheet1['H1'] = column_titles_sheet1[7]
sheet1['I1'] = column_titles_sheet1[8]
sheet1['J1'] = column_titles_sheet1[9]
sheet1['K1'] = column_titles_sheet1[10]
sheet1['L1'] = column_titles_sheet1[11]
sheet1['M1'] = column_titles_sheet1[12]
sheet1['N1'] = column_titles_sheet1[13]
sheet1['O1'] = column_titles_sheet1[14]
sheet1['P1'] = column_titles_sheet1[15]
sheet1['Q1'] = column_titles_sheet1[16]
sheet1['R1'] = column_titles_sheet1[17]

wb.save(filename='Golf_Statistics.xlsx')

# for i in column_titles_sheet1:
#     headers = sheet1.cell(row=1, column=1)
#     headers.value = column_titles_sheet1[i]
#     wb.save(filename='Golf_Statistics.xlsx')

# For loops that add the column titles to the sheets in order
# for col_num, data in enumerate(column_titles_sheet1):
#     sheet1.write(0, col_num, data)
#
# for col_num, data in enumerate(column_titles_sheet2):
#     sheet2.write(0, col_num, data)
#
# for col_num, data in enumerate(column_titles_sheet3):
#     sheet3.write(0, col_num, data)

master = Tk()
master.title("Golf Statistics")
master.geometry("700x300")
master.configure(background="white")

#Header of the Program
main_header = Label(master, text="Golf Statistics")
main_header.config(font =("Times New Roman", 30))
main_header.grid(row=0, column=0)

#Entry for name
Label(master, text='First Name and Last Name').grid(row=2)
name = Entry(master)
name.grid(row=2, column=1)

def name_user():
    entry_name = name.get()
    print(entry_name)
    sheet1['A2'] = entry_name
    wb.save(filename='Golf_Statistics.xlsx')

#Entry for Date
Label(master, text='Date').grid(row=3)
date = Entry(master)
date.grid(row=3, column=1)

def date_of_user():
    entry_date = date.get()
    print(entry_date)
    sheet1['B2'] = entry_date
    wb.save(filename='Golf_Statistics.xlsx')

#Individual notes about golfer
Label(master, text='Individual notes about golfer').grid(row=8)
notes = Entry(master)
notes.grid(row=8, column=1)

def user_notes():
    entry_notes = notes.get()
    print(entry_notes)
    sheet1['C2'] = entry_notes
    wb.save(filename='Golf_Statistics.xlsx')

def average_distance():
    newWindow = Toplevel(master)
    newWindow.title("Calculate Average Distance")
    newWindow.geometry("900x200")
    #Header
    main_header = Label(newWindow, text="Average Distance of a Golf Club")
    main_header.config(font=("Times New Roman", 20))
    main_header.grid(row=0, column=0)
    #Buttons
    Button(newWindow, text="Graph", command= lambda: average_distance_bar_chart(distance, club_name)).grid(row=3, column=0)
    Button(newWindow, text="Calculate", command= lambda: claculate_average_distance(distance, club_name)).grid(row=4, column=1)
    # Label and entry for club and distance of golf shots
    Label(newWindow, text='Enter one of the following clubs (Driver, 3-Wood, 5-Wood, 3-Iron, 4-Iron, 5-Iron,\n'
                          '6-Iron, 7-Iron, 8-Iron, 9-Iron, Pitching Wedge, Gap Wdge, Sand Wedge, Lob Wedge, Putter)?').grid(row=1)
    Label(newWindow, text='Enter Distance of Golf Shots (Ex: 400 + 200 + 100)').grid(row=2)
    club_name = Entry(newWindow)
    distance = Entry(newWindow)
    club_name.grid(row=1, column=1)
    distance.grid(row=2, column=1)

def claculate_average_distance(distance, club_name):
    entry_club_name = club_name.get()
    entry_distance = distance.get()
    # This is a for loop to count the amount of times the + character is in the entry for distance
    value = 0
    for x in entry_distance:
        if x == '+':
            value = value + 1
    number_of_symbols = value + 1
    average_yards = (eval(entry_distance) / number_of_symbols)
    print("You are able to hit your", entry_club_name, "an average distance of", round(average_yards, 2), "yards!")

    if entry_club_name == column_titles_sheet1[3]:
        sheet1['D2'] = average_yards
    if entry_club_name == column_titles_sheet1[4]:
        sheet1['E2'] = average_yards
    if entry_club_name == column_titles_sheet1[5]:
        sheet1['F2'] = average_yards
    if entry_club_name == column_titles_sheet1[6]:
        sheet1['G2'] = average_yards
    if entry_club_name == column_titles_sheet1[7]:
        sheet1['H2'] = average_yards
    if entry_club_name == column_titles_sheet1[8]:
        sheet1['I2'] = average_yards
    if entry_club_name == column_titles_sheet1[9]:
        sheet1['J2'] = average_yards
    if entry_club_name == column_titles_sheet1[10]:
        sheet1['K2'] = average_yards
    if entry_club_name == column_titles_sheet1[11]:
        sheet1['L2'] = average_yards
    if entry_club_name == column_titles_sheet1[12]:
        sheet1['M2'] = average_yards
    if entry_club_name == column_titles_sheet1[13]:
        sheet1['N2'] = average_yards
    if entry_club_name == column_titles_sheet1[14]:
        sheet1['O2'] = average_yards
    if entry_club_name == column_titles_sheet1[15]:
        sheet1['P2'] = average_yards
    if entry_club_name == column_titles_sheet1[16]:
        sheet1['Q2'] = average_yards
    if entry_club_name == column_titles_sheet1[17]:
        sheet1['R2'] = average_yards
    # for i in column_titles_sheet1:
    #     if entry_club_name != column_titles_sheet1[i]:
    #         print("Enter a Valid Club Name")
    wb.save(filename='Golf_Statistics.xlsx')


def average_distance_bar_chart(distance, club_name):
    entry_distance = distance.get()
    entry_club_name = club_name.get()
    value = 0
    for x in entry_distance:
        if x == '+':
            value = value + 1
    number_of_symbols = value + 1
    average_yards = (eval(entry_distance) / number_of_symbols)

    plt.barh([entry_club_name],
             [round(average_yards, 2)], align='center', label="Distance")
    plt.legend()

    plt.xlim([0, 500])
    plt.ylabel('Type of Golf Club')
    plt.xlabel('Distance (yds)')
    plt.title('Average Distance of ' + entry_club_name)

    plt.show()

def accuracy_of_shot():
    newWindow = Toplevel(master)
    newWindow.title("Calculate Accuracy")
    newWindow.geometry("700x200")
    #Header
    main_header = Label(newWindow, text="Accuracy of a Golf Club")
    main_header.config(font=("Times New Roman", 20))
    main_header.grid(row=0, column=0)
    #Buttons
    Button(newWindow, text="Graph", command= lambda: accuruacy_pie_chart(accuracy, name_of_club)).grid(row=3, column=0)
    Button(newWindow, text="Calculate", command= lambda: calculate_accuracy(name_of_club, accuracy)).grid(row=3, column=1)
    #Label and entry for accuracy of a shot
    Label(newWindow, text='What Club Are You Using?').grid(row=1)
    Label(newWindow, text='Enter the type of shot you hit (Hook, Slice, Fade, Draw, Push, Pull)').grid(row=2)
    name_of_club = Entry(newWindow)
    accuracy = Entry(newWindow)
    name_of_club.grid(row=1, column=1)
    accuracy.grid(row=2, column=1)

def calculate_accuracy(name_of_club, accuracy):
    entry_name_of_club = name_of_club.get()
    entry_accuracy = accuracy.get()

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
    if Hook > 0:
        print("You will hit a hook shot with your", entry_name_of_club, round(result_hook, 2), "% of the time out of", len(entry_accuracy.split()), "shots!")
    if Slice > 0:
        print("You will hit a slice shot with your", entry_name_of_club, round(result_slice, 2), "%% of the time out of", len(entry_accuracy.split()), "shots!")
    if Fade > 0:
        print("You will hit a fade shot with your", entry_name_of_club, round(result_fade, 2), "% of the time out of", len(entry_accuracy.split()), "shots!")
    if Draw > 0:
        print("You will hit a draw shot with your", entry_name_of_club, round(result_draw, 2), "% of the time out of", len(entry_accuracy.split()), "shots!")
    if Push > 0:
        print("You will hit a push shot with your", entry_name_of_club, round(result_push, 2), "% of the time out of", len(entry_accuracy.split()), "shots!")
    if Pull > 0:
        print("You will hit a pull shot with your", entry_name_of_club, round(result_pull, 2), "% of the time out of", len(entry_accuracy.split()), "shots!")

#Pie Chart for the accuracy of a golf club
# I am having some trouble with the appearance of my graph
def accuruacy_pie_chart(accuracy, name_of_club):
    entry_name_of_club = name_of_club.get()
    entry_accuracy = accuracy.get()

    # Counter for the occurrences of the different accuracies in the entry
    Hook = entry_accuracy.count("Hook")
    Slice = entry_accuracy.count("Slice")
    Fade = entry_accuracy.count("Fade")
    Draw = entry_accuracy.count("Draw")
    Push = entry_accuracy.count("Push")
    Pull = entry_accuracy.count("Pull")

    labels = 'Hook', 'Slice', 'Fade', 'Draw', "Push", "Pull"
    sizes = [Hook, Slice, Fade, Draw, Push, Pull]
    explode = (0, 0.1, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title('Accuracy of ' + entry_name_of_club)
    plt.show()

def percentage_chance_of_putt():
    newWindow = Toplevel(master)
    newWindow.title("Calculate Chance of Making a Putt")
    newWindow.geometry("600x200")

    # Header
    main_header = Label(newWindow, text="Chance of Making a Putt")
    main_header.config(font=("Times New Roman", 20))
    main_header.grid(row=0, column=0)

    # Buttons
    Button(newWindow, text="Graph", command=lambda: chance_of_making_putt_pie_chart(length, amount_of_putts)).grid(row=3, column=0)
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

    # Printing result of calculations
    if result_one_putt > 0:
        print("You will have a", round(result_one_putt, 2), "% change of making a one putt from", entry_length, "away!")
    if result_two_putt > 0:
        print("You will have a", round(result_two_putt, 2), "% change of making a two putt from", entry_length, "away!")
    if result_three_putt > 0:
        print("You will have a", round(result_three_putt, 2), "% change of making a three putt from", entry_length, "away!")
    if result_four_putt > 0:
        print("You will have a", round(result_four_putt, 2), "% change of making a four putt from", entry_length, "away!")
    if result_five_putt > 0:
        print("You will have a", round(result_five_putt, 2), "% change of making a five putt from", entry_length, "away!")
    if result_six_putt > 0:
        print("You will have a", round(result_six_putt, 2), "% change of making a six putt from", entry_length, "away!")
    if result_seven_putt > 0:
        print("You will have a", round(result_seven_putt, 2), "% change of making a seven putt from", entry_length, "away!")
    if result_eight_putt > 0:
        print("You will have a", round(result_eight_putt, 2), "% change of making a eight putt from", entry_length, "away!")
    if result_nine_putt > 0:
        print("You will have a", round(result_nine_putt, 2), "% change of making a nine putt from", entry_length, "away!")


#Pie Chart for the percentage chance of making a putt from a certain distance
# I am having some trouble with the appearance of my graph
def chance_of_making_putt_pie_chart(length, amount_of_putts):
    entry_length = length.get()
    entry_amount_of_putts = amount_of_putts.get()

    # Counter for the occurrences of the number of putts to make it into the hole.
    One_Putt = entry_amount_of_putts.count("1")
    Two_Putt = entry_amount_of_putts.count("2")
    Three_Putt = entry_amount_of_putts.count("3")
    Four_Putt = entry_amount_of_putts.count("4")
    Five_Putt = entry_amount_of_putts.count("5")
    Six_Putt = entry_amount_of_putts.count("6")
    Seven_Putt = entry_amount_of_putts.count("7")
    Eight_Putt = entry_amount_of_putts.count("8")
    Nine_Putt = entry_amount_of_putts.count("9")

    labels = "One Putt", "Two Putt", "Three Putt", "Four Putt", "Five Putt", "Six Putt", "Seven Putt", "Eight Putt", "Nine Putt"
    sizes = [One_Putt, Two_Putt, Three_Putt, Four_Putt, Five_Putt, Six_Putt, Seven_Putt, Eight_Putt, Nine_Putt]
    explode = (0, 0.1, 0, 0, 0, 0, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title("Percentage Chance of Making a Putt from " + entry_length + " Away")
    plt.show()

# Function that calls a file to run a paint program
def tracking_consistency():
    runpy.run_path(path_name='Tracking_Consistency_Paint_File.py')

#Place holder function for graphs
def place_holder():
    print("hi")

# Function to open excel file
def open_excel_file():
    df = pd.read_excel('Golf_Statistics.xlsx')
    print(df)

# Function to exit code
def exit_program():
    exit()

#Buttons
Button(master, text="Calculate Average Distance of Golf Club",command=average_distance).grid(row=4)
Button(master, text="Calculate the Accuracy of a Golf Club",command=accuracy_of_shot).grid(row=5)
Button(master, text="Calculate the Percentage Chance of Making a Putt",command=percentage_chance_of_putt).grid(row=6)
Button(master, text="Tracking Consistency",command=tracking_consistency).grid(row=7)
Button(master, text="Exit",command=exit_program).grid(row=9, column=1)
Button(master, text="View Xlsx Data",command=open_excel_file).grid(row=9, column=2)
Button(master, text="Download",command=place_holder).grid(row=9, column=0)
Button(master, text="Enter",command=name_user).grid(row=2, column=2)
Button(master, text="Enter",command=date_of_user).grid(row=3, column=2)
Button(master, text="Enter",command=user_notes).grid(row=8, column=2)

master.mainloop()
