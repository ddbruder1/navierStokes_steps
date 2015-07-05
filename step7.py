# Step 7 2D Diffusion
# Dmitriy Bruder
# 07/04/2015
# execute using: ipython step7.py

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import sympy as spy

nx = 31
ny = 31
nt = 17
nu = 0.05
dx = 2.0/(nx-1)
dy = 2.0/(ny-1)
sigma = 0.25
dt = sigma*dx*dy/nu

x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)

u = np.ones((ny, nx))
un = np.ones((ny, nx))


def diffuse(nt):
    u[0.5/dy:1/dy+1, 0.5/dx:1/dx+1] = 2

    for n in range(nt+1):
        un = u.copy()
        u[1:-1, 1:-1] = un[1:-1, 1:-1] \
            + (nu*dt/dx**2*(un[1:-1, 2:]-2*un[1:-1, 1:-1] + un[1:-1, 0:-2])) \
            + (nu*dt/dy**2*(un[2:, 1:-1]-2*un[1:-1, 1:-1] + un[0:-2, 1:-1]))

        u[0, :] = 1
        u[-1, :] = 1
        u[:,  0] = 1
        u[:, -1] = 1

    fig = plt.figure(figsize=(11, 7), dpi = 100)
    ax = fig.gca(projection='3d')
    X, Y = np.meshgrid(x, y)
    surf = ax.plot_surface(X, Y, u[:], rstride=1, cstride=1, \
            cmap=cm.coolwarm, linewidth=0, antialiased=True)
    ax.set_ylim(0, 2)
    ax.set_xlim(0, 2)
    ax.set_zlim(1, 2.5)
    plt.show()

# get user input, convert to int and store in 'temesteps' variable
timesteps = int(input("Please enter the desired number of time steps: "))
# call diffuse function, passing in timesteps for 'nt'
diffuse(timesteps)


