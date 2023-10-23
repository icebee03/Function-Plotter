import sys
import time

import matplotlib.pyplot as plt
import numpy as np
from tkinter import *
import customtkinter as ctk


def f(x):
    return 2 * x ** 2 + 3 * x + 5


def firstplot():
    x, y = [], []
    for i in range(-10, 10, 1):
        x.append(i)
        y.append(f(i))

    plt.plot(x, y, color="r")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(r"Plot of $2x^2 + 3x + 5$")  # TeX format inside dollar signs
    plt.show()


def plotFunction(x, y, name):
    plt.plot(x, y, color = "r")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Plot of function ${name}$")
    plt.show()


def initCTkValues(app):
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("green")
    app.geometry("500x500")
    #button = ctk.CTkButton(master=app, text="Hello World!")
    #button.place(relx=0.5, rely=0.5, anchor=CENTER)


def main():
    app = ctk.CTk()
    initCTkValues(app)

    entry = ctk.CTkEntry(app, placeholder_text="Enter your values")
    entry.place(relx=.5, rely=.5, anchor= CENTER)
    time.sleep(1)
    arg = entry.get()
    args = arg.split()
    print(args)


    polynomial = []
    for i in range(0, len(args), 2):
        polynomial.append(int(args[i][0]))

    x, y = [], []
    for i in range(-20, 20):
        x.append(i)
        y.append(np.polyval(polynomial, i))

    #plotFunction(x, y, arg)
    app.mainloop()




if __name__ == "__main__":
    main()
