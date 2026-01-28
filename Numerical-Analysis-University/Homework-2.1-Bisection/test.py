import math

def f(x):
    return math.sqrt(4 + (5 * math.sin(x))) - 2.5
x1 = float(input("what is the first bound you would like to test"))
x2 = float(input("what is the second bound you would like to test"))

def output(a,b):
    fa, fb = f(a), f(b)
    if fa==0 or fb==0 or fa * fb < 0:
        print("there is a guranteed root in the ")
    else:
        print("there is no guranteed root")

output(x1, x2)

print(f"the outputs are \n{f(x1)} \nand \n{f(x2)}.")