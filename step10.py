# Step 10 Poisson Eq for pressure
# Dmitriy Bruder
# 07/09/2015

# NOTE: This eq is not protting correctly

import numpy as np
import sympy as spy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# declare variables
nx = 50
ny = 50
nt = 200
xmin = 0.0
xmax = 2.0
ymin = 0.0
ymax = 1.0

dx = (xmax - xmin)/(nx-1)
dy = (ymax - ymin)/(ny-1)

# Init
p = np.zeros((ny, nx))
pn = np.zeros((ny, nx))
b = np.zeros((ny, nx))
x = np.linspace(xmin, xmax, nx)
y = np.linspace(ymin, ymax, ny)

# Source
b[ny/4, nx/4] = 100
b[3*ny/4, 3*nx/4] = -100

for it in range(nt):
    pn = p.copy()
    p[1:-1, 1:-1] = (dy**2*(pn[1:-1,2:]+pn[1:-1, :-2]) \
                    + dx**2*(pn[2:, 1:-1]+pn[:-2, 1:-1]) \
                    - b[1:-1, 1:-1]*dx**2*dy**2) \
                    /(2*(dx**2 + dx**2))
    p[0, :] = 0.0 ##p = 0 @ y = 0
    p[ny-1, :] = 0.0 ##p = 0 @ y = 1
    p[:, 0] = 0.0 ##p = 0 @ x = 0
    p[:, nx-1] = 0.0 ##p = 0 # x = 2

# function to produce 3D projection plot
# takes 3 arguments: x-vector, y-vector, p-matrix
def plot2d(x, y, p):
    # set figure properties
    fig = plt.figure(figsize=(11, 7), dpi = 100)
    # set figure type
    ax = fig.gca(projection = "3d")
    # create x,y grid
    X, Y = np.meshgrid(x,y)
    # plot p in the x,y grid
    surf = ax.plot_surface(X, Y, p[:], rstride=1, cstride=1, \
                           cmap=cm.coolwarm, linewidth=0, antialiased=False)
    # set plot limits
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    # set initial viewing angle
    ax.view_init(30, 225)
    plt.show()

plot2d(x, y, p)

