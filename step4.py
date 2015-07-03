# Step 4 Burgers Equation "Convection and Diffusion"
# Dmitriy Bruder
# 07/03/2015

import numpy as np
import matplotlib.pyplot as plt
import sympy #symbolic math lib
from sympy.utilities.lambdify import lambdify

#define x, nu and t as symbols
x, nu, t = sympy.symbols("x nu t")
#define phi equation using symbols
phi = sympy.exp(-(x-4*t)**2/(4*nu*(t+1)))+sympy.exp(-(x-4*t-2*np.pi)**2/(4*nu*(t+1)))
print phi
#take the derivity of phi w.r.t. x
phiprime = phi.diff(x)
print phiprime
#initial condition
u = -2*nu*(phiprime/phi)+4
print u
#turn u into a function with t, x, and nu arguments (using lambdify)
ufunc = lambdify((t, x, nu),u)
print ufunc(1,2,3)

#begin numerical scheme
#define scheme variables
nx = 101
nt = 100
dx = 2.0*np.pi/(nx-1)
nu = 0.07
dt = dx*nu
#create even incraments of x from 0 to 2pi
x = np.linspace(0, 2*np.pi, nx)
#empty both u and un arrays
u = np.empty(nx)
un = np.empty(nx)
t = 0
# convert ufunc into an array and solve for each x
u = np.asarray([ufunc(t,x0,nu) for x0 in x])
print u
#plot the initial condition
plt.figure(figsize=(11,7), dpi=100)
plt.plot(x,u, marker='o', lw=2)
plt.xlim([0,2*np.pi])
plt.ylim([0,10]);
plt.show()
#pause, wait for user input
raw_input()

#begin numerical scheme
for n in range(nt):
    un = u.copy()
    for i in range(nx-1):
        u[i]= un[i]-un[i]*dt/dx*(un[i]-un[i-1])+nu*dt/dx**2* \
            (un[i+1]-2*un[i]+un[i-1])

        u[-1]= un[-1]-un[-1]*dt/dx*(un[-1]-un[-2])+nu*dt/dx**2* \
            (un[0]-2*un[-1]+un[-2])

u_computational = np.asarray([ufunc(nt*dt,xi,nu)for xi in x])

plt.figure(figsize=(11,7), dpi = 100)
plt.plot(x,u,marker = "o",lw = 2, label = "Computational")
plt.plot(x, u_computational, label = "Analytical")
plt.xlim([0, 2*np.pi])
plt.ylim([0,10])
plt.legend()
plt.show()



