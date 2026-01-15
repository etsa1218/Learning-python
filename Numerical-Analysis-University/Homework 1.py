import math


def g(x):
    return (x**2 + x)**(1/3)


phi = (1 + math.sqrt(5)) / 2

g(phi) == phi
