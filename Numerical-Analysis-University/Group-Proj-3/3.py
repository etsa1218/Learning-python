from Main_bisect import bisect
import math


def f(x):
    return math.pi * (x ** 2) * (1 - (x / 3)) - 1


height = bisect(0, 1, f, 1E-3)
print(f"the height is {height}")
