from adaptiveintegrate import adaptive as adp
import math

# define function


def f(x): return math.log(x + 1)


value, interval = adp(f, 0, 1, 1E-6)

print(
    f"the value of the integral is {value}\n and the number of intervals is {interval}")
