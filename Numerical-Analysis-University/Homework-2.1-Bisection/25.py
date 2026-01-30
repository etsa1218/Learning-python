import math
from main_bisect import bisect

def f(x):
    return math.sin((x ** 2))
root = bisect(7,8,f,1e-8)

print(f"the root is{root}")
print(f"the f(root) is {f(root)}")