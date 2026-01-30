import math
from main_bisect import bisect

def f(x): 
    return math.log((x**4) - (x**3) - (7 * (x **2)) + (13 * x) - 5)
root = bisect(0.8,1.2,f,1e-8)
print(f"the root is {root}")
print(f"the value of f(root) is {f(root)}")
