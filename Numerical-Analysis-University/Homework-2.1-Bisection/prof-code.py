import math
from typing import Callable

def bisection(a: float, b: float, f: Callable[[float], float], tol: float) -> float:
    if not (a < b):
        raise ValueError("Require a < b.")

    # Compute iteration count exactly as in your Octave code
    N = math.ceil((math.log(b - a) - math.log(tol)) / math.log(2))

    L = f(a)
    m = (a + b) / 2.0  # define in case N == 0 (corner case)

    for _ in range(N):
        m = (a + b) / 2.0
        M = f(m)

        # Exact-zero check (rare in floating-point, but preserved from Octave)
        if M == 0.0:
            return m

        if L * M < 0.0:
            b = m
        else:
            a = m
            L = M

    return m