from tkinter import *
root = Tk()
from matplotlib import pyplot as plt
def first_graph(x, y):
    # x = [5, 2, 9, 4, 7]
    # y = [10, 5, 8, 4, 2]

    plt.plot(x, y)
    plt.show()

def get_values():
    input_x = input()
    input_y = input()
    input_x = int(input_x)
    input_y = int(input_y)
    input_x1 = input()
    input_y1 = input()
    input_x1 = int(input_x1)
    input_y1 = int(input_y1)

    x = [input_x, input_x1]
    y = [input_y, input_y1]
    first_graph(x, y)


Button(root, text = "Testbutton", command = get_values).grid(row=0, column=0)
root.mainloop()