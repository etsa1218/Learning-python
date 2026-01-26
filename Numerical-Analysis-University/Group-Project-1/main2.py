#%%
import matplotlib.pyplot as plt
import numpy as np
#importing necessary plotting tools

#defining function
def fun(x):
    return (np.e ** x) - np.cos(x) - x
#defining x and y values
x_values = np.linspace((-5 * (10 ** -8)), (5 * (10 ** -8)), 1000)
y_values = fun(x_values)

#making the graph
plt.plot(x_values, y_values, label = 'plot of f(x)')
plt.grid(True)
plt.show
# the graph is very jagged when it should be smooth.
#this would be due to floating point error
#as there is only 16 sigfigs with both approximations
#of e and cos(x)


# %%
