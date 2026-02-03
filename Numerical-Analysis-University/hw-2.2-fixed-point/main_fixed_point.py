import math
from typing import Callable

#function definition
def fp(x_0: float,g: Callable[[float], float], tol: float, max_it: int=1000 ) -> tuple[float, int]:
    #fixed point iteration g(x)=x_n+1
    x_n = x_0
    
    #loop
    for count in range(1, max_it + 1):
        x_nplus1 = g(x_n)

        #stopping criteria
        if abs(x_nplus1 - x_n) < tol:
            return x_nplus1, count
        
        x_n = x_nplus1
        

    
    raise RuntimeError("Fixed Point did not converge")

