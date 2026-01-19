import numpy as np
T_3 = lambda x: 1 + x + ((1/2) * x ** 2) + ((1/6) * x ** 3)

print(f"T_3(0) = {T_3(0)}")
print(f"T_3(3/2) = {T_3(3/2)}")
print(f"T_3(2) = {T_3(2)}")
print(f"T_3(e) = {T_3(np.e)}")

