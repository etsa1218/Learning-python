import math
from typing import Callable

# function definition


def seca(x0: float, f: Callable[[float], float], tol: float, maxit: float = 1000) -> float:
    # Setting up vars
    y0 = f(x0)
    x1 = x0 + y0
    y1 = f(x1)
    for j in range(maxit):
        # division by 0 protection
        if y1 - y0 == 0:
            raise ValueError("Cannot divide by 0")
        # checking if value is reached
        x = x1 - (y1 * ((x1 - x0) / (y1 - y0)))
        if abs(x - x1) <= tol:
            return x, j

        x0 = x1
        y0 = y1
        x1 = x
        y1 = f(x1)
    raise RuntimeError("secant method failed, max iterations reached")
