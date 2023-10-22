import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return 2 * x ** 2 + 3 * x + 5


def main():
    x, y = [], []
    for i in range(-10, 10, 1):
        x.append(i)
        y.append(f(i))

    plt.plot(x, y, color="r")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(r"Plot of $2x^2 + 3x + 5$")       #TeX format inside dollar signs
    plt.show()


if __name__ == "__main__":
    main()
