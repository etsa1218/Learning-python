from main_fixed_point import fp
def g(x):
    return (3 * x ** 2 - 1) / (6 * x + 4)

root, iterations = fp(-2, g, 1E-2)

print(f"the fixed point is {root}")
print(f"the number of iterations it took is {iterations}")
