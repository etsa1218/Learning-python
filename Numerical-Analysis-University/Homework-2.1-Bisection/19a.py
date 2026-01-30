#%%
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.log((x ** 4) - (x ** 3) - (7 * (x ** 2)) + (13 * x) - 5)

x_values = np.linspace(0.8,1.2,100)
y_values = f(x_values)

plt.plot(x_values, y_values)
plt.grid(True)
plt.show()



# %%
