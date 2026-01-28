import math

#2a
#function definition and inputs
def f(x):
    return 3 - x - math.sin(x)
x1 = float(input("what is the first bound you would like to test"))
x2 = float(input("what is the second bound you would like to test"))

#function calling and output
def output(a,b):
    fa, fb = f(a), f(b)
    if fa==0 or fb==0 or fa * fb < 0:
        print("there is a guranteed root in the interval.")
    else:
        print("there is no guranteed root in the interval.")

output(x1, x2)

print(f"The ouputs are \n{f(x1)} \nand \n{f(x2)}")

#2e
