from tkinter import *
from matplotlib import pyplot as plt
import numpy as np

master = Tk()
master.title("Matplotlib & Tkinter")
master.geometry("200x200")
master.configure(background = "deep sky blue")


#Line Graph
def line_graph(x, y):
    plt.plot(x, y)
    plt.show()

#Inputs are not working for some reasons
def input_for_line_graph():
    for i in range(5):
        input_x = input(i)
        input_x = int(input_x)
    for i in range(5):
        input_y = input(i)
        input_y = int(input_y)
    x = [input_x]
    y = [input_y]
    line_graph(x, y)


#Pie Chart
def pie_chart():
    accuracy = ["Hook", "Straight", "Draw", "Slice", "Fade", "Straight", "Hook", "Straight", "Hook", "Draw", "Straight"]
    driv_hook = (accuracy.count("Hook"))
    driv_fade = (accuracy.count("Fade"))
    driv_slice = (accuracy.count("Slice"))
    driv_draw = (accuracy.count("Draw"))
    driv_straight = (accuracy.count("Straight"))
    labels = 'Hook', 'Fade', 'Slice', 'Draw', "Straight"
    sizes = [driv_hook, driv_fade, driv_slice, driv_draw, driv_straight]
    explode = (0, 0.1, 0, 0, 0)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')
    plt.title('Accuracy of Driver')
    plt.show()

#Horizontal Bar Chart
def bar_chart():
    driv1 = 300
    driv2 = 250
    driv3 = 275
    avg_driver = (driv1+driv2+driv3) / 3

    threewood1 = 300
    threewood2 = 250
    threewood3 = 275
    avg_3_wood = (threewood1+threewood2+threewood3) / 3

    fouriron1 = 190
    fouriron2 = 180
    fouriron3 = 213
    avg_4_iron = (fouriron1 + fouriron2 + fouriron3) / 3

    seveniron1 = 175
    seveniron2 = 184
    seveniron3 = 163
    avg_7_iron = (seveniron1 + seveniron2 + seveniron3) / 3

    nineiron1 = 154
    nineiron2 = 146
    nineiron3 = 139
    avg_9_iron = (nineiron1 + nineiron2 + nineiron3) / 3

    plt.barh(["Driver", "3 Wood", "4 Iron", "7 Iron", "9 Iron"],
             [avg_driver, avg_3_wood, avg_4_iron, avg_7_iron, avg_9_iron], align='center', label="Distance")
    plt.legend()

    plt.xlim([0, 500])
    plt.ylabel('Different Clubs')
    plt.xlabel('Distance')
    plt.title('Average Distance of Golf Clubs')

    plt.show()

#Data Comparison Bar Chart
def data_comparison_bar_chat():
    # data to plot
    driver_first_year = [238, 243, 247, 254]
    driver_second_year = [255, 263, 268, 271]

    # create plot
    fig, ax = plt.subplots()
    bar_width = 0.35
    X = np.arange(4)

    p1 = plt.bar(X, driver_first_year, bar_width, color='b',
                 label='First Year')

    # The bar of second plot starts where the first bar ends
    p2 = plt.bar(X + bar_width, driver_second_year, bar_width,
                 color='g',
                 label='Second Year')

    plt.ylim([0, 400])
    plt.ylabel('Distance')
    plt.title('Average Driver Distance')
    plt.xticks(X + (bar_width / 2), ("September", "December",
                                     "February", "May"))
    plt.legend()

    plt.tight_layout()
    plt.show()

Button(master, text="Line Graph", command=input_for_line_graph).grid(row=0, column=0)
Button(master, text="Pie Chart", command=pie_chart).grid(row=0, column=1)
Button(master, text="Horizontal Bar Chart", command=bar_chart).grid(row=3, column=0)
Button(master, text="Data Comparison", command=data_comparison_bar_chat).grid(row=5, column=0)

master.mainloop()