'''
CFD ME702 Step 4 // 1D Burgers Eq // Covection and diffusion

'''
"Start Setting up initial conditions"
import numpy as np
import sympy #formats the equations
from sympy import init_printing 
init_printing(use_latex=True)

x, nu, t = sympy.symbols('x nu t')
phi = sympy.exp(-(x-4*t)**2/(4*nu*(t+1)))+sympy.exp(-(x-4*t-2*np.pi)**2/(4*nu*(t+1))) #define phi
phi #in ipython notebook will print out the eq

phiprime = phi.diff(x) #derivative of phi w.r.t x
phiprime #in ipython notebook will print out the eq
print ("\n" + "Phi Prime: " + str(phiprime) + "\n")

from sympy.utilities.lambdify import lambdify #lambdify takes SymPy symbolic eq and 
#turns it into a calleble function

u = -2*nu*(phiprime/phi)+4
print ("u: " + str(u) + "\n")

ufunc = lambdify((t, x, nu), u)
print ("ufunc: " + str(ufunc(1,4,3)) + "\n")
"End Setting up initial conditions"

import matplotlib.pyplot as plt

"""init variables"""
nx = 101#number of points in the grid
dx = 2*np.pi/(nx-1) #distance between adjacent grid points (dx) 0.05 * 50 steps
nt = 100 #number of time steps
nu = .07 #viscosity term
dt = dx*nu #lenght of time step, dt is calculated with respect to dx

x = np.linspace(0, 2*np.pi, nx)
#u = np.empty(nx)
un = np.empty(nx)
t = 0 

u = np.asarray([ufunc(t, x0, nu) for x0 in x])
#print u
'''
plt.figure(figsize=(11,7), dpi = 100)
plt.plot(x,u, marker = 'o', lw = 2)
plt.xlim([0,2*np.pi])
plt.ylim([0,10]);
'''
for n in range(nt):
    un = u.copy()
    for i in range(nx-1):
        u[i] = un[i]-un[i]*dt/dx*(un[i]-un[i-1])+nu*dt/dx**2*(un[i+1]-2*un[i]+un[i-1])
        u[-1] = un[-1]-un[-1]*dt/dx*(un[-1]-un[-2])+nu*dt/dx**2*(un[0]-2*un[-1]+un[-2])

u_analytical = np.asarray([ufunc(nt*dt, xi, nu) for xi in x])

plt.figure(figsize=(8,5), dpi = 100)
plt.plot(x,u, marker = 'o', lw = 2, label='analytical')
plt.plot(x, u_analytical, label='computational')
plt.xlim([0,2*np.pi])
plt.ylim([0,10])
plt.legend();
        
