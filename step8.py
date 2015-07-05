# Step 8 2D Convection and DIffusion
# Dmitriy Bruder
# 07/05/2015

import numpy as np
import matplotlib.pyplot as plt
import sympy as spy
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

nx = 41
ny = 41
nt = 120
nu = 0.01
dx = 2.0/(nx-1)
dy = 2.0/(ny-1)
sigma = 0.0009
dt = sigma*dx*dy/nu

x = np.linspace(0, 2, nx)
y = np.linspace(0, 2, ny)

u = np.ones((ny, nx))
v = np.ones((ny, nx))
un = np.ones((ny, nx))
vn = np.ones((ny, nx))
comb = np.ones((ny, nx))

u[0.5/dy:1/dy+1, 0.5/dx:1/dx+1] = 2
v[0.5/dy:1/dy+1, 0.5/dx:1/dx+1] = 2

def solve():
    for n in range(nt):
        un = u.copy()
        vn = v.copy()

        u[1:-1, 1:-1] = un[1:-1, 1:-1] \
            - dt/dx*un[1:-1, 1:-1]*(un[1:-1, 1:-1]-un[1:-1, 0:-2]) \
            - dt/dy*vn[1:-1, 1:-1]*(un[1:-1, 1:-1]-un[0:-2, 1:-1]) \
            + nu*dt/dx**2*(un[1:-1, 1:-1]-2*un[1:-1, 1:-1]+un[1:-1, 0:-2]) \
            + nu*dt/dy**2*(un[1:-1, 1:-1]-2*un[1:-1, 1:-1]+un[0:-2, 1:-1])
        v[1:-1, 1:-1] = vn[1:-1, 1:-1] \
            - dt/dx*un[1:-1, 1:-1]*(vn[1:-1, 1:-1]-vn[1:-1, 0:-2]) \
            - dt/dy*vn[1:-1, 1:-1]*(vn[1:-1, 1:-1]-vn[0:-2, 1:-1]) \
            + nu*dt/dx**2*(vn[1:-1, 1:-1]-2*vn[1:-1, 1:-1]+vn[1:-1, 0:-2]) \
            + nu*dt/dy**2*(vn[1:-1, 1:-1]-2*vn[1:-1, 1:-1]+vn[0:-2, 1:-1])

        u[0, :] = 1
        u[-1, :] = 1
        u[:, 0] = 1
        u[:, -1] = 1

        v[0, :] = 1
        v[-1, :] = 1
        v[:, 0] = 1
        v[:, -1] = 1

    fig = plt.figure(figsize=(11,7), dpi=100)
    ax = fig.gca(projection="3d")
    X, Y = np.meshgrid(x, y)
    wire1 = ax.plot_wireframe(X, Y, u)
    wire2 = ax.plot_wireframe(X, Y, v)
   # ax.set_ylim(0, 2)
   # ax.set_xlim(0, 2)
   # ax.set_zlim(1, 2.5)
    plt.show()

solve()
