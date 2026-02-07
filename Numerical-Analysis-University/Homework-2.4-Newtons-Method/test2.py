from main_secant import seca
import math


def f(y):
    return ((y - 2) ** 2) - math.log(y)


root, iters = seca(3.2, f, 1e-5)
print(f"the root is {root}")
print(f"the iterations taken was {iters}")
