# Step 1 1D linear Convection
# Dmitriy Bruder
# 07/01/2015
# execute using: ipython file.py

import numpy as np
import matplotlib.pyplot as plt

# decclare and init variables
nx = 41 #number of steps
nt = 25 #number of time steps
c = 1.0 #transport velocity
sigma = 0.5 #CFL
dx = 2.0/(nx - 1) #space step
dt = sigma*dx/c #time step using CFL

# initial conditions
u =  np.ones(nx)
# u = 2 0.5 <= x(i) <= 1  else u = 1
u[0.5/dx : 1/dx+1] = 2
# plot initial condition
plt.plot(np.linspace(0,2,nx),u)

# declare array to store temp values for u
un = np.ones(nx)

# Numerical scheme: F.D. in time, B.D. in space
# step through time
for n in range(1, nt):
    #copy the values in u into the temp array
    un = u.copy()
    for i in range(1,nx):
        # step in space using the dicretized eq
        u[i] = un[i]-c*(dt/dx)*(un[i]-un[i-1])
#plot the output
plt.plot(np.linspace(0,2,nx),u)
# display plot it using ipython console
plt.show()
