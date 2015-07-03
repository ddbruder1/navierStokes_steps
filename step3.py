# Step 3 1D Diffusion
# Dmitriy Bruder
# 07/02/2015

import numpy as np
import matplotlib.pyplot as plt
import math as mth

nx = 41 #number of space steps
nt = 20 #number of time steps
nu = 0.3 #viscous term
sigma = 0.2 #CFL
dx = 2.0/(nx-1) #incrament of space
dt = sigma*dx**2/nu #incrament of time

u = np.ones(nx)

u[0.5/dx : 1/dx-1]=2

plt.plot(np.linspace(0,2,nx),u) #plot initial condition

un = np.ones(nx)

for n in range(nt):
    un = u.copy()
    for i in range(nx-1):
        u[i] = un[i]+nu*dt/dx**2*(un[i+1]-2*un[i]+un[i-1])
plt.plot(np.linspace(0,2,nx),u) #plot numerical solution
plt.show() #necessary to display plot in ipython console
