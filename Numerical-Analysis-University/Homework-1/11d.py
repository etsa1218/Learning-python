import math


def g(x):
    return (x**2 + x)**(1/3)


numba = (1 + math.sqrt(5)) / 2

print(g(numba) == numba)
