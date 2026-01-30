import math
from main_bisect import bisect
def f(x): 
    return math.sin(math.e ** x) + x
root = bisect(-3,3,f,1e-8)
print(f"the root is {root}")
print(f"the value of f(root) is {f(root)}")