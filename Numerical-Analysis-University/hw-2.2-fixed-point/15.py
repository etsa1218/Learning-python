from main_fixed_point import fp
import math

def cbrt(x):
    return math.copysign(abs(x)**(1/3), x)

def F(x):
    return cbrt(3 * x - 3)

root, iterations = fp(-1, F, 1E-4)

print(f"the root is {root}")
print(f"the iterations it took is {iterations}")
def h(x):
    return x ** 3 - 3 * x + 3
print(abs(h(root)))