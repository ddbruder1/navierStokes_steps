# Step 2 1D non-linear Convectin
# Dmitriy Bruder
# 07/02/2015
# execute using: ipython file.py
# see Step 1 for comments
import numpy as np
import matplotlib.pyplot as plt

# declare variables
nx = 101
nt = 25
sigma = 0.5
dx = 2.0/(nx-1)
dt = sigma*dx

u = np.ones(nx)

u[0.5/dx : 1/dx-1] = 2

plt.plot(np.linspace(0,2,nx),u)

un = np.ones(nx)

for n in range(nt):
    un = u.copy()
    for i in range(nx):
        u[i] = un[i]-un[i]*(dt/dx)*(un[i]-un[i-1])

plt.plot(np.linspace(0,2,nx),u)
plt.show()
