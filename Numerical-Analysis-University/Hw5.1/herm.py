import numpy as np
import sympy as sp

#data
t_data = [0,3,5,8,13]
x_data = [0,225,383,623,993]
s_data = [75,77,80,74,72]

#hermite divided difference
def herm_div(x,y,yp):
    #def rows and data pts
    n = len(x)
    m = 2*n
    
    z = [0]*m
    Q = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(n):
        z[2*i] = x[i]
        z[2*i + 1] = x[i]

        Q[2*i][0] = y[i]
        Q[2*i + 1][0] = y[i]

        Q[2*i + 1][1] = yp[i]
        
        if i == 0:
            Q[2*i][1] = yp[i]
        else:
            Q[2*i][1] = (Q[2*i][0] - Q[2*i-1][0]) / (z[2*i] - z[2*i - 1])
    for j in range(2, m):
        for i in range(j,m):
            Q[i][j] = (Q[i][j-1] - Q[i - 1][j - 1]) / (z[i] - z[i - j])
    return z, Q

