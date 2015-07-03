# Step 3 1D Diffusion
# Dmitriy Bruder
# 07/02/2015

import numpy as np
import matplotlib.pyplot as plt
import math as mth

nx = 21
nt = 100
nu = 0.15
sigma = 0.2
dx = 2.0/(nx-1)
dt = sigma*dx**2/nu

#sigma = raw_input("Please enter a value for sigma: \n")

print dt
u = np.ones(nx)

u[0.5/dx : 1/dx-1]=2
print u
plt.plot(np.linspace(0,2,nx),u)


for n in range(nt):
    un = u.copy()
    for i in range(nx-1):
        u[i] = un[i]+nu*dt/dx**2*(un[i+1]-2*un[i]+un[i+1])
plt.plot(np.linspace(0,2,nx),u)
plt.show()
