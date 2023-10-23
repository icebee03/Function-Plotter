import sys
import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 2 * x ** 2 + 3 * x + 5


def run(p, x):
    value = np.polyval(p, x)
    return value


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


def main():
    args = sys.argv[1:]
    arg = ""
    for i in range(len(args)):
        arg += args[i] + " "

    polynomial = []
    for i in range(0, len(args), 2):
        polynomial.append(int(args[i][0]))

    x, y = [], []
    for i in range(-20, 20):
        x.append(i)
        y.append(np.polyval(polynomial, i))

    plotFunction(x, y, arg)


if __name__ == "__main__":
    main()
