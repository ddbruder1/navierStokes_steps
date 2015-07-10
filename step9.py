# Step 9 Laplace Eq for pressure
# Dmitriy Bruder
# 07/08/2015

import numpy as np
import sympy as spy
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

# ***** Function Declaration ******

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
    ax.set_ylim(0, 1)
    # set initial viewing angle
    ax.view_init(30, 225)
    plt.show()

# Laplace C.D. numerical scheme function
# l1norm_target:  how close the p-matrix should be in two consecutive --
# -- iterations before the loop breaks and returns the calculated value
def laplace2d(p, y, dx, dy, l1norm_target):
    l1norm = 1
    pn = np.empty_like(p)

    while l1norm > l1norm_target:
        pn = p.copy()
        p[1:-1, 1:-1] = (dy**2*(pn[1:-1,2:]+pn[1:-1, 0:-2]) \
                         + dx**2*(pn[2:, 1:-1]+pn[0:-2, 1:-1])) \
                        /(2*(dx**2 + dx**2))
        p[:, 0] = 0 ##p = 0 @ x = 0
        p[:, -1] = y ##p = y @ x = 2 p[0, :] = p[1, :] ##dp/dy = 0 @ y = 0
        p[-1, :] = p[-2, :] ##dp/dy = 0 # y = 1
        l1norm = (np.sum(np.abs(p[:])-np.abs(pn[:])))/np.sum(np.abs(pn[:]))

    return p


# ****** Main Program ******

# declare variables
nx = 31
ny = 31
c = 1
dx = 2.0/(nx-1)
dy = 2.0/(ny-1)

# Plottting aids
x = np.linspace(0, 2, nx)
y = np.linspace(0, 1, ny)

# Create a XxY vector of 0's
p = np.zeros((ny, nx))

p[:, 0] = 0 ##p = 0 @ x = 0
p[:, -1] = y ##p = y @ x = 2
p[0, :] = p[1, :] ##dp/dy = 0 @ y = 0
p[-1, :] = p[-2, :] ##dp/dy = 0 # y = 1

# solve for p using the laplace
p = laplace2d(p, y, dx, dy, 1e-4)
plot2d(x, y, p)

