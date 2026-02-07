import math
from typing import Callable


def newt(x0: float, f: Callable[[float], float], fprime: Callable[[float], float], tol: float, maxiter: float = 1000) -> tuple[float, int]:
    x = x0
    for j in range(maxiter):
        fx = f(x)
        fprimex = fprime(x)

        if fprimex == 0:
            raise ValueError("cannot divide by 0, fprime(x) = 0")
        step = fx / fprimex
        x1 = x - step

        if abs(x1 - x) < tol:
            return x1, j

        x = x1
    raise RuntimeError("max iterations reached")
