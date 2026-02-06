from main_newton import newt
import math
print("starting")


def f(y):
    return (math.exp(y)) + (2 ** (-y)) + (2 * (math.cos(y))) - 6


def fprime(y):
    return (math.exp(y)) - (math.log(2) / (2 ** y)) - (2 * math.sin(y))


print("before newt")
root, iters = newt(1.5, f, fprime, 1E-5)
print(f"the root is {root}")
print(f"the number of iterations is {iters}")
