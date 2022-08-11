import numpy as np


def h(n):
    if n == 0:
        return 1.0
    elif n == 1:
        return -0.5
    else:
        return 5 * (-1 / 2) ** n


def sum():
    return h(0) + h(1)+ (h(2)/(1+(1/2)))


print(sum())
