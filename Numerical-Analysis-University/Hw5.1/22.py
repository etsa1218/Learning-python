from herm import herm_div
import numpy as np
import sympy as sp

t_data = [0,3,5,8,13]
x_data = [0,225,383,623,993]
s_data = [75,77,80,74,72]

#building polynomial
def herm_poly(x,y,yp):
    z, Q = herm_div(x,y,yp)
    t = sp.symbols('t')

    H = Q[0][0]
    product = 1
    
    for i in range(1, len(z)):
        product *= (t-z[i-1])
        H += Q[i][i] * product

    return sp.expand(H), z, Q

#building the position poly
t = sp.symbols('t')
H, z, Q = herm_poly(t_data, x_data, s_data)
print('hermite poly s(t):\n',H)

H_prime = sp.expand(sp.diff(H, t))

print("\n Speed polynomial s'(t):\n", H_prime)

# hermite poly s(t):
# -2.02236319728923e-5*t**9 + 0.00104059023036464*t**8 
#- 0.0218756663126486*t**7 + 0.243041247850604*t**6 - 1.53829559927047*t**5 
# + 5.5081205113349*t**4 - 10.0953089386411*t**3 + 7.16190803747534*t**2 + 75*t

#
# part b
#
d_at_10 = sp.N(H.subs(t, 10))
s_at_10 = sp.N(H_prime.subs(t,10))
print(f"at t = 10 \n speed = {s_at_10}\n and distance is {d_at_10}")
#speed at 10 is 48.3817363639537
#distance at 10 is 742.502839098775

#
#part c
#

s_lim = 55 * (5280/3600)

eq = sp.expand(H_prime - s_lim)

roots = sp.nroots(eq)

real_roots = []

for r in roots:
    if abs(sp.im(r)) < 1e-8:
        real_part = float(sp.re(r))
        if 0<= real_part <= 13:
            real_roots.append(real_part)
real_roots.sort()

print("times where speed = 55mph")
print(real_roots)

#test intervals around roots to see if it exceeds 55
test_pts = [0]
for rt in real_roots:
    test_pts.append(rt)
test_pts.append(13)

#check mids
exceeds = False

first_exceed = None

int_pts = [0] + real_roots + [13]
for i in range(len(int_pts) - 1):
    a = int_pts[i]
    b = int_pts[i + 1]
    mid = (a + b) / 2
    val = float(H_prime.subs(t, mid))
    if val > s_lim:
        exceeds = True
        first_exceed = a
        break
print("\n Does car exceed 55 mph?", exceeds)
if exceeds:
    print(f"First time exceeded is t ={first_exceed}")

#the car exceeds at 55 at 5.648802541921842 seconds

#
#part d
#

H_sec = sp.expand(sp.diff(H_prime, t))
crit_roots = sp.nroots(H_sec)

crit_pts = []
for k in crit_roots:
    if abs(sp.im(k)) < 1e-8:
        real_pt = float(sp.re(k))
        if 0 <= real_pt <= 13:
            crit_pts.append(real_pt)
crit_pts.sort()

#eval speed at crit pts and end
cand = [0,13] + crit_pts
values = [(pt, float(H_prime.subs(t, pt))) for pt in cand]
max_pt, max_s = max(values, key=lambda x: x[1])

print("\n Crit pts for speed are")
print(crit_pts)

print("\nCandidate speeds")
for pt, val in values:
    print(f"t = {pt:.6f}, speed = [val:.6f] ft/s")
print(f"\nPredicted max speed is {max_s:.6f} ft/s at t = {max_pt: .6f} s")
