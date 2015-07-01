'''
CFD ME702 Step 3 // 1D Diffusion // heat equation if u = temp

in this eq:  exponentially damped wave
Using: Forward Diff in time from n to n+1
       Central Diff in space from i+1 to i-1
Initial conditions: u=2 at 0.5<= x <=1
                    u=1 everywhere else in (0,2)
Boundary conditions: u=1 at x=0, x=2
'''

import numpy as np
import matplotlib.pyplot as plt
#import time as sys

#%matplotlib inline #dispay results in line in ipython notebook
"""init variables"""
nx = 41#number of points in the grid
dx = 2.0/(nx-1) #distance between adjacent grid points (dx) 0.05 * 50 steps
nt = 20 #number of time steps
nu = .3 #viscosity term
sigma = 0.2 #Courant number, insures stability
dt = sigma*dx**2/nu #lenght of time step, dt is calculated with respect to dx

"""establish initial conditions"""
u = np.ones(nx) #define an array which with nx elements in lenght
u[0.5/dx : 1/dx+1]=2 # initial condition u = 2 at 0.5 <= x <= 1

plt.plot(np.linspace(0,2,nx),u) #plot the initial condition

un = np.ones(nx) #init temporary array to store the values of u @ time n
for n in range(nt): #run the loop nt times (0 to nt) iterate in time
    un = u.copy() #copy the value of u(array) into un(array)
    for i in range(1,nx-1):
       """the main eq"""       
       u[i] = un[i]+nu*dt/dx**2*(un[i+1]-2*un[i]+un[i-1])
       
print u       
plt.plot(np.linspace(0,2,nx),u);
