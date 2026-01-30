import math
from main_bisect import bisect
#4a
def f(x): 
    return 3 - math.sin(x) - x
root = bisect(2,3,f,1e-8)
print(f"the root is {root}")
print(f"the value of f(root) is {f(root)}")

#4e
def f(x): 
    return math.sqrt(4 + (5 * math.sin(x))) - 2.5
root = bisect(-6,-5,f,1e-8)
print(f"the root is {root}")
print(f"the value of f(root) is {f(root)}")

#4i
def f(x): 
    return math.sin(math.e ** x) + x
root = bisect(-3,3,f,1e-8)
print(f"the root is {root}")
print(f"the value of f(root) is {f(root)}")