import math
from typing import Callable
# this is defining the bisection method


def bisect(a: float, b: float, f: Callable[[float], float], tol: float) -> float:
    # This is to make sure the error bounds make sense
    if not a < b:
        raise ValueError("must be a < b")
    if f(a) * f(b) > 0:
        raise ValueError("f(a) * f(b) must be less than or equal to 0")
    # this is to calculate the amount of iterations it takes
    N = math.ceil(((math.log(b-a))-math.log(tol))/math.log(2))

    L = f(a)
    m = (a + b) / 2.0

    for _ in range(N):
        m = (a+b) / 2
        M = f(m)
    # zero check
        if M == 0.0:
            return m
        if L * M < 0:
            b = m
        else:
            a = m
            L = M
    return m
