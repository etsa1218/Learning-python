from main_newton import newt
import math


def f(y):
    return ((y - 2) ** 2) - math.log(y)


def fprime(y):
    return (2 * (y - 2)) - (1 / y)


root, iters = newt(3.3, f, fprime, 1E-5)
print(f"the root is {root}")
print(f"the number of iterations is {iters}")
